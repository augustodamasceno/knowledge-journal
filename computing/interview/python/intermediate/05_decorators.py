"""Decorators: wrapping functions, factory decorators, class decorators."""
import functools
import time
import logging


# ── 1. Basic function decorator ───────────────────────────────────────────────
def timer(func):
    @functools.wraps(func)   # preserves __name__, __doc__, __annotations__
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timer] {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n: int) -> int:
    return sum(range(n))

print(slow_sum(1_000_000))

# ── 2. Decorator with arguments (factory) ──────────────────────────────────────
def retry(times: int = 3, delay: float = 0.0,
          exceptions: tuple = (Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    logging.warning(f"{func.__name__} attempt {attempt} failed: {e}")
                    if attempt < times and delay:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError, TimeoutError))
def unstable_fetch(url: str) -> str:
    import random
    if random.random() < 0.5:
        raise ConnectionError("network hiccup")
    return f"content from {url}"

# ── 3. Stacking decorators ────────────────────────────────────────────────────
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kw_str   = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kw_str]))
        print(f"→ {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} = {result!r}")
        return result
    return wrapper

@timer
@debug
def add(a: int, b: int) -> int:
    return a + b

add(3, b=4)

# ── 4. Class-based decorator ──────────────────────────────────────────────────
class Memoize:
    def __init__(self, func):
        self.func  = func
        self.cache = {}
        functools.update_wrapper(self, func)  # copy __name__ etc.

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

    def cache_clear(self):
        self.cache.clear()

@Memoize
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(30))
print(fib.cache)

# ── 5. Decorator that works on classes ────────────────────────────────────────
def add_repr(cls):
    """Auto-generate __repr__ from __init__ annotations."""
    fields = list(cls.__init__.__annotations__.keys())
    def __repr__(self):
        parts = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{cls.__name__}({parts})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Config:
    def __init__(self, host: str, port: int, debug: bool = False):
        self.host  = host
        self.port  = port
        self.debug = debug

print(Config("localhost", 8080, True))  # Config(host='localhost', port=8080, debug=True)

# ── 6. Preserving introspection ───────────────────────────────────────────────
print(slow_sum.__name__)       # slow_sum  (not wrapper)
print(slow_sum.__wrapped__)    # original function (set by functools.wraps)
