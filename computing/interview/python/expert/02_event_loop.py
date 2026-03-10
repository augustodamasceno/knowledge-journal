"""Minimal event loop: illustrating asyncio internals from scratch."""
import heapq
import selectors
import time
from collections import deque
from typing import Callable


# ── Future: a placeholder for a result that isn't yet available ───────────────
class Future:
    def __init__(self):
        self._result   = None
        self._done     = False
        self._callbacks: list[Callable] = []

    def set_result(self, result):
        if self._done:
            raise RuntimeError("Future already resolved")
        self._result = result
        self._done   = True
        for cb in self._callbacks:
            cb(self)

    def result(self):
        if not self._done:
            raise RuntimeError("Future not yet resolved")
        return self._result

    def done(self) -> bool:
        return self._done

    def add_done_callback(self, cb: Callable):
        if self._done:
            cb(self)
        else:
            self._callbacks.append(cb)

    # Makes Future awaitable in an async context
    def __await__(self):
        if not self._done:
            yield self          # suspend; event loop will resume us
        return self._result


# ── Task: wraps a coroutine and drives it step by step ───────────────────────
class Task:
    def __init__(self, coro, loop: "SimpleEventLoop"):
        self._coro   = coro
        self._loop   = loop
        self._future = Future()
        self._loop.call_soon(self._step)

    def _step(self, incoming=None):
        try:
            # Resume the coroutine; it may yield a Future to wait on
            yielded = self._coro.send(incoming)
            if isinstance(yielded, Future):
                yielded.add_done_callback(lambda f: self._step(f.result()))
            else:
                # coroutine yielded None: schedule next step immediately
                self._loop.call_soon(self._step)
        except StopIteration as exc:
            self._future.set_result(exc.value)

    def result(self):
        return self._future.result()


# ── SimpleEventLoop ───────────────────────────────────────────────────────────
class SimpleEventLoop:
    def __init__(self):
        self._ready:     deque = deque()
        self._scheduled: list  = []     # min-heap of (deadline, seq, callback, args)
        self._selector           = selectors.DefaultSelector()
        self._seq                = 0    # tie-break for same deadline

    def call_soon(self, callback: Callable, *args):
        self._ready.append((callback, args))

    def call_later(self, delay: float, callback: Callable, *args):
        deadline = time.monotonic() + delay
        heapq.heappush(self._scheduled, (deadline, self._seq, callback, args))
        self._seq += 1

    def create_task(self, coro) -> Task:
        return Task(coro, self)

    def _run_once(self):
        # Promote due scheduled callbacks to the ready queue
        now = time.monotonic()
        while self._scheduled and self._scheduled[0][0] <= now:
            _, _, cb, args = heapq.heappop(self._scheduled)
            self._ready.append((cb, args))

        # Execute all currently ready callbacks (snapshot count)
        n = len(self._ready)
        for _ in range(n):
            cb, args = self._ready.popleft()
            cb(*args)

    def run_until_complete(self, coro):
        task = self.create_task(coro)
        while not task._future.done():
            if not self._ready and self._scheduled:
                sleep_time = max(0.0, self._scheduled[0][0] - time.monotonic())
                time.sleep(sleep_time)
            self._run_once()
        return task.result()

    def close(self):
        self._selector.close()


# ── Demo ──────────────────────────────────────────────────────────────────────
def make_delay(loop: SimpleEventLoop, seconds: float) -> Future:
    """Equivalent of asyncio.sleep — returns a Future resolved after delay."""
    fut = Future()
    loop.call_later(seconds, fut.set_result, None)
    return fut


async def greet(loop: SimpleEventLoop, name: str, delay: float) -> str:
    await make_delay(loop, delay)
    msg = f"Hello, {name}! (after {delay}s)"
    print(msg)
    return msg


async def main(loop: SimpleEventLoop):
    t0 = time.monotonic()
    # Run two greetings concurrently via tasks
    t1 = loop.create_task(greet(loop, "Alice", 0.2))
    t2 = loop.create_task(greet(loop, "Bob",   0.1))

    await make_delay(loop, 0.3)   # wait long enough for both to finish
    print(f"Both done in {time.monotonic()-t0:.2f}s")
    return t1.result(), t2.result()


if __name__ == "__main__":
    loop   = SimpleEventLoop()
    result = loop.run_until_complete(main(loop))
    print(f"Results: {result}")
    loop.close()
