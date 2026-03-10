"""Thread safety: locks, RLock, Condition, Event, Semaphore, and queue."""
import threading
import time
import random
import queue


# ── Lock ──────────────────────────────────────────────────────────────────────
class SafeSet:
    """A thread-safe set."""
    def __init__(self):
        self._data: set = set()
        self._lock = threading.Lock()

    def add(self, item) -> None:
        with self._lock:
            self._data.add(item)

    def discard(self, item) -> None:
        with self._lock:
            self._data.discard(item)

    def __contains__(self, item) -> bool:
        with self._lock:
            return item in self._data

    def __len__(self) -> int:
        with self._lock:
            return len(self._data)


ss = SafeSet()
threads = [threading.Thread(target=ss.add, args=(i,)) for i in range(1000)]
for t in threads: t.start()
for t in threads: t.join()
print(f"SafeSet size: {len(ss)}")   # 1000


# ── RLock: re-entrant lock ────────────────────────────────────────────────────
class TreeNode:
    def __init__(self, val):
        self.val      = val
        self.children = []
        self._lock    = threading.RLock()   # reentrant

    def add_child(self, node: "TreeNode") -> None:
        with self._lock:
            self.children.append(node)

    def count_nodes(self) -> int:
        with self._lock:   # can re-acquire in recursive call
            return 1 + sum(c.count_nodes() for c in self.children)


# ── Event: one-shot signal ────────────────────────────────────────────────────
start_event = threading.Event()

def worker(name: str):
    print(f"{name}: waiting for start signal...")
    start_event.wait()           # blocks until event is set
    print(f"{name}: started!")

threads = [threading.Thread(target=worker, args=(f"W{i}",)) for i in range(3)]
for t in threads: t.start()
time.sleep(0.1)
print("Main: firing start event")
start_event.set()                # unblocks all waiting threads
for t in threads: t.join()


# ── Condition: wait / notify ──────────────────────────────────────────────────
BUFFER      = []
MAX_BUF     = 5
cond        = threading.Condition()
TOTAL_ITEMS = 10

def producer():
    for i in range(TOTAL_ITEMS):
        with cond:
            while len(BUFFER) >= MAX_BUF:
                cond.wait()
            BUFFER.append(i)
            cond.notify()
        time.sleep(random.uniform(0, 0.02))

def consumer():
    received = 0
    while received < TOTAL_ITEMS:
        with cond:
            while not BUFFER:
                cond.wait()
            item = BUFFER.pop(0)
            received += 1
            cond.notify()
        # process item
    print(f"Consumer received {received} items")

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start()
p.join();  c.join()


# ── Semaphore: rate limiter ───────────────────────────────────────────────────
class RateLimiter:
    """Allow at most `rate` calls per `period` seconds."""
    def __init__(self, rate: int, period: float = 1.0):
        self._sem    = threading.Semaphore(rate)
        self._rate   = rate
        self._period = period
        self._lock   = threading.Lock()

    def acquire(self):
        self._sem.acquire()
        threading.Timer(self._period, self._sem.release).start()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *_):
        pass


# ── queue.Queue: thread-safe FIFO ────────────────────────────────────────────
q: queue.Queue = queue.Queue(maxsize=10)

def multi_producer(items: int, q: queue.Queue):
    for i in range(items):
        q.put(i)
        time.sleep(0.005)
    q.put(None)   # sentinel

def multi_consumer(q: queue.Queue):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        # process
        q.task_done()

mp = threading.Thread(target=multi_producer, args=(20, q))
mc = threading.Thread(target=multi_consumer, args=(q,))
mp.start(); mc.start()
mp.join();  mc.join()
q.join()   # blocks until all task_done() have been called
print("Queue processing complete")


# ── threading.local: per-thread storage ──────────────────────────────────────
_local = threading.local()

def task_with_local(name: str):
    _local.name = name          # each thread has its own _local.name
    time.sleep(random.uniform(0, 0.02))
    print(f"Thread {threading.current_thread().name}: local.name = {_local.name}")

threads = [threading.Thread(target=task_with_local, args=(f"task-{i}",)) for i in range(4)]
for t in threads: t.start()
for t in threads: t.join()
