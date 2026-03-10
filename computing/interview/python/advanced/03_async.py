"""asyncio: coroutines, tasks, gather, semaphore, async generators."""
import asyncio
import time
import random


# ── Basic coroutine ──────────────────────────────────────────────────────────
async def greet(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Hello, {name}!"

# asyncio.run() is the entry point for top-level coroutines
result = asyncio.run(greet("Alice", 0))
print(result)


# ── Concurrent execution with gather ──────────────────────────────────────────
async def demo_gather():
    t0 = time.perf_counter()
    results = await asyncio.gather(
        greet("Alice", 0.3),
        greet("Bob",   0.1),
        greet("Carol", 0.2),
    )
    print(results)
    print(f"Total: {time.perf_counter()-t0:.2f}s")   # ~0.3s, not 0.6s

asyncio.run(demo_gather())


# ── Tasks: fire-and-forget ────────────────────────────────────────────────────
async def background_worker(name: str, n: int):
    for i in range(n):
        await asyncio.sleep(0.05)
        print(f"  {name}: step {i}")

async def demo_tasks():
    t1 = asyncio.create_task(background_worker("worker-1", 3))
    t2 = asyncio.create_task(background_worker("worker-2", 3))
    await asyncio.gather(t1, t2)

asyncio.run(demo_tasks())


# ── Timeout ───────────────────────────────────────────────────────────────────
async def slow_operation():
    await asyncio.sleep(5)
    return "done"

async def demo_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.1)
    except asyncio.TimeoutError:
        print("Operation timed out")

asyncio.run(demo_timeout())


# ── Semaphore: limit concurrent operations ────────────────────────────────────
async def fetch(url: str, sem: asyncio.Semaphore) -> str:
    async with sem:
        delay = random.uniform(0.05, 0.15)
        await asyncio.sleep(delay)    # simulate HTTP request
        return f"200 OK from {url}"

async def demo_semaphore():
    sem  = asyncio.Semaphore(3)      # max 3 concurrent
    urls = [f"http://example.com/{i}" for i in range(10)]
    results = await asyncio.gather(*[fetch(u, sem) for u in urls])
    for r in results:
        print(r)

asyncio.run(demo_semaphore())


# ── Async context manager ─────────────────────────────────────────────────────
class AsyncDB:
    async def __aenter__(self):
        await asyncio.sleep(0.01)   # simulate connect
        print("DB connected")
        return self

    async def __aexit__(self, *_):
        await asyncio.sleep(0.01)   # simulate disconnect
        print("DB disconnected")

    async def query(self, sql: str) -> list:
        await asyncio.sleep(0.01)
        return [{"id": 1}, {"id": 2}]

async def demo_async_cm():
    async with AsyncDB() as db:
        rows = await db.query("SELECT * FROM users")
        print(rows)

asyncio.run(demo_async_cm())


# ── Async generator ───────────────────────────────────────────────────────────
async def paginate(total: int, page_size: int):
    for start in range(0, total, page_size):
        await asyncio.sleep(0.01)   # simulate DB page fetch
        yield list(range(start, min(start + page_size, total)))

async def demo_async_gen():
    async for page in paginate(25, 10):
        print(f"Page: {page}")

asyncio.run(demo_async_gen())


# ── asyncio.Queue: producer-consumer ──────────────────────────────────────────
async def producer(queue: asyncio.Queue, items: int):
    for i in range(items):
        await asyncio.sleep(0.05)
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)   # sentinel

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(0.02)
        print(f"Consumed {item}")
        queue.task_done()

async def demo_queue():
    q = asyncio.Queue(maxsize=5)
    await asyncio.gather(producer(q, 6), consumer(q))

asyncio.run(demo_queue())
