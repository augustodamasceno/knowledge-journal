"""Context managers: class-based, @contextmanager, and contextlib helpers."""
import time
from contextlib import contextmanager, suppress, ExitStack, redirect_stdout
import io


# ── Class-based context manager ───────────────────────────────────────────────
class Timer:
    def __init__(self, label: str = ""):
        self.label   = label
        self.elapsed = 0.0

    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        return self             # bound to `as` target

    def __exit__(self, exc_type, exc_val, traceback) -> bool:
        self.elapsed = time.perf_counter() - self._start
        print(f"{self.label} elapsed: {self.elapsed:.6f}s")
        return False            # False = re-raise any exception


with Timer("list creation") as t:
    lst = list(range(1_000_000))

print(f"captured: {t.elapsed:.6f}s")

# ── @contextmanager ───────────────────────────────────────────────────────────
@contextmanager
def managed_file(path: str, mode: str = "r"):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

# with managed_file("data.txt", "w") as f:
#     f.write("hello")

# ── Nested context managers (single with) ─────────────────────────────────────
# with open("a.txt") as a, open("b.txt") as b:
#     ...

# ── contextlib.suppress ───────────────────────────────────────────────────────
with suppress(FileNotFoundError, IsADirectoryError):
    open("nonexistent.txt")

# ── redirect_stdout ───────────────────────────────────────────────────────────
buf = io.StringIO()
with redirect_stdout(buf):
    print("captured output")
print(f"Got: {buf.getvalue()!r}")

# ── ExitStack: dynamic number of context managers ─────────────────────────────
files = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    # Opens each file that exists; stack ensures all are closed
    handles = []
    for path in files:
        try:
            handles.append(stack.enter_context(open(path)))
        except FileNotFoundError:
            pass

# ── Reusable / re-entrant context managers ────────────────────────────────────
import threading

class RLockContext:
    """RLock as a context manager (threading.RLock already is one, this is illustrative)."""
    def __init__(self):
        self._lock = threading.RLock()
        self._depth = 0

    def __enter__(self):
        self._lock.acquire()
        self._depth += 1
        return self

    def __exit__(self, *_):
        self._depth -= 1
        self._lock.release()
        return False

# ── @contextmanager with cleanup on exception ─────────────────────────────────
@contextmanager
def transaction(conn):
    """Commit on success, rollback on exception."""
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# ── Demonstrate __exit__ suppression ─────────────────────────────────────────
class SuppressAll:
    def __enter__(self): return self
    def __exit__(self, *_): return True   # suppress all exceptions

with SuppressAll():
    raise RuntimeError("this is swallowed")

print("Execution continues after suppressed exception")
