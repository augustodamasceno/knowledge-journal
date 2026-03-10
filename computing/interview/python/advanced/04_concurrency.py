"""Concurrency: threading, multiprocessing, and concurrent.futures."""
import threading
import multiprocessing
import concurrent.futures
import time
import queue as queue_module


# ── Threading: I/O-bound work ─────────────────────────────────────────────────
def io_task(name: str, delay: float) -> str:
    time.sleep(delay)            # releases GIL during sleep
    return f"{name} done after {delay}s"

threads = [
    threading.Thread(target=io_task, args=(f"task-{i}", 0.2))
    for i in range(5)
]
t0 = time.perf_counter()
for t in threads: t.start()
for t in threads: t.join()
print(f"5 × 0.2s tasks ran in {time.perf_counter()-t0:.2f}s")  # ~0.2s


# ── Thread-safe counter ───────────────────────────────────────────────────────
class SafeCounter:
    def __init__(self):
        self._value = 0
        self._lock  = threading.Lock()

    def increment(self, n: int = 1):
        with self._lock:
            self._value += n

    @property
    def value(self) -> int:
        with self._lock:
            return self._value

counter = SafeCounter()
threads = [threading.Thread(target=counter.increment) for _ in range(1000)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Counter: {counter.value}")   # 1000


# ── Condition variable: producer-consumer ─────────────────────────────────────
BUFFER_SIZE  = 5
buffer: list = []
cond         = threading.Condition()

def producer(items: int):
    for i in range(items):
        with cond:
            while len(buffer) >= BUFFER_SIZE:
                cond.wait()
            buffer.append(i)
            cond.notify_all()
        time.sleep(0.01)

def consumer(items: int):
    consumed = 0
    while consumed < items:
        with cond:
            while not buffer:
                cond.wait()
            item = buffer.pop(0)
            consumed += 1
            cond.notify_all()

p = threading.Thread(target=producer, args=(10,))
c = threading.Thread(target=consumer, args=(10,))
p.start(); c.start()
p.join();  c.join()
print("Producer-consumer finished")


# ── Semaphore: limit concurrent threads ───────────────────────────────────────
sem = threading.Semaphore(3)   # max 3 threads at once

def limited_task(idx: int):
    with sem:
        time.sleep(0.1)
        print(f"Task {idx} finished")

threads = [threading.Thread(target=limited_task, args=(i,)) for i in range(9)]
for t in threads: t.start()
for t in threads: t.join()


# ── ThreadPoolExecutor ────────────────────────────────────────────────────────
def fetch(url: str) -> str:
    time.sleep(0.1)    # simulate network call
    return f"200 from {url}"

urls = [f"http://example.com/{i}" for i in range(8)]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(fetch, urls))
print(results)


# ── ProcessPoolExecutor: CPU-bound ────────────────────────────────────────────
def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def find_primes(start: int, end: int) -> list[int]:
    return [n for n in range(start, end) if is_prime(n)]

# Split work across processes
ranges = [(i*100_000, (i+1)*100_000) for i in range(4)]

if __name__ == "__main__":   # required guard for multiprocessing on Windows
    with concurrent.futures.ProcessPoolExecutor() as ex:
        futures = [ex.submit(find_primes, s, e) for s, e in ranges]
        all_primes = []
        for f in concurrent.futures.as_completed(futures):
            all_primes.extend(f.result())
    print(f"Found {len(all_primes)} primes in [0, 400000)")


# ── as_completed: process results as they finish ─────────────────────────────
import random

def slow_task(n: int) -> int:
    time.sleep(random.uniform(0.05, 0.2))
    return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    fmap = {ex.submit(slow_task, i): i for i in range(10)}
    for future in concurrent.futures.as_completed(fmap):
        src = fmap[future]
        print(f"  {src}^2 = {future.result()}")


# ── multiprocessing.Value + Lock ──────────────────────────────────────────────
def worker(shared_val, lock):
    for _ in range(1000):
        with lock:
            shared_val.value += 1

if __name__ == "__main__":
    val  = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()
    procs = [multiprocessing.Process(target=worker, args=(val, lock))
             for _ in range(4)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(f"Shared counter: {val.value}")   # 4000
