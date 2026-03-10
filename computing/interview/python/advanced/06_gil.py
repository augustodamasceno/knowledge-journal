"""The GIL: demonstration, impact, and workarounds."""
import sys
import time
import threading
import multiprocessing


# ── Check GIL (Python 3.13+ only) ────────────────────────────────────────────
if sys.version_info >= (3, 13):
    print(f"GIL enabled: {sys._is_gil_enabled()}")


# ── CPU-bound: threads do NOT parallelize ────────────────────────────────────
def cpu_work(n: int = 10_000_000) -> int:
    return sum(range(n))

def time_it(target, repeat: int = 2) -> float:
    t0 = time.perf_counter()
    for _ in range(repeat):
        target()
    return time.perf_counter() - t0

def run_threaded(n_threads: int, work) -> float:
    threads = [threading.Thread(target=work) for _ in range(n_threads)]
    t0 = time.perf_counter()
    for t in threads: t.start()
    for t in threads: t.join()
    return time.perf_counter() - t0

serial_time   = time_it(cpu_work, repeat=2)
threaded_time = run_threaded(2, cpu_work)
print(f"Serial   (×2): {serial_time:.2f}s")
print(f"Threaded (×2): {threaded_time:.2f}s  ← similar or worse due to GIL")


# ── I/O-bound: threads DO help (GIL released during I/O wait) ────────────────
def io_work(delay: float = 0.1) -> None:
    time.sleep(delay)   # GIL is released here

serial_io   = time_it(lambda: io_work(0.2), repeat=4)
threaded_io = run_threaded(4, lambda: io_work(0.2))
print(f"\nSerial   I/O (×4): {serial_io:.2f}s")
print(f"Threaded I/O (×4): {threaded_io:.2f}s  ← ~4× faster")


# ── Fix: use multiprocessing for CPU-bound work ───────────────────────────────
def multiprocess_work(n_procs: int) -> float:
    t0 = time.perf_counter()
    with multiprocessing.Pool(n_procs) as pool:
        pool.map(cpu_work, [1] * n_procs)  # trivial work to show overhead
    return time.perf_counter() - t0

# (Commented out to avoid spawning processes at module import time)
# if __name__ == "__main__":
#     mp_time = multiprocess_work(2)
#     print(f"Multiprocess (×2): {mp_time:.2f}s")


# ── Thread-safety implications ────────────────────────────────────────────────
# The GIL does NOT make all operations atomic.
# Example: += on a list is NOT atomic (read-modify-write is multiple bytecodes)
import dis
print("\nBytecode for 'x += 1':")
dis.dis("x += 1")

# This means you still need locks for mutable shared state:
counter = 0
lock    = threading.Lock()

def unsafe_increment():
    global counter
    for _ in range(100_000):
        counter += 1    # NOT atomic; race condition even with GIL in some cases

def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

# ── GIL release in C extensions ──────────────────────────────────────────────
# numpy, pandas, and many C extensions explicitly release the GIL during
# computation, so numpy operations DO run in parallel across threads.
try:
    import numpy as np
    a = np.random.rand(1000, 1000)

    def numpy_work():
        np.linalg.svd(a)   # C code, releases GIL

    serial_np   = time_it(numpy_work, repeat=2)
    threaded_np = run_threaded(2, numpy_work)
    print(f"\nNumPy serial  (×2): {serial_np:.2f}s")
    print(f"NumPy threaded(×2): {threaded_np:.2f}s  ← may be faster!")
except ImportError:
    print("\nnumpy not installed; skipping numpy GIL demo")
