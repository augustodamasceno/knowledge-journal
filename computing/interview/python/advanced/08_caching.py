"""Caching: lru_cache internals, manual LRU, and memoisation patterns."""
from __future__ import annotations
from collections import OrderedDict
from functools import lru_cache, cache
import threading
import time


# ── functools.lru_cache ───────────────────────────────────────────────────────
@lru_cache(maxsize=128)
def expensive(n: int) -> int:
    """Fibonacci with caching."""
    return n if n < 2 else expensive(n - 1) + expensive(n - 2)

print([expensive(i) for i in range(12)])
print(expensive.cache_info())   # CacheInfo(hits=..., misses=..., maxsize=128, currsize=...)
expensive.cache_clear()

# cache (Python 3.9+): unbounded, slightly faster than lru_cache(maxsize=None)
@cache
def binomial(n: int, k: int) -> int:
    if k == 0 or k == n: return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

print(binomial(20, 10))  # 184756


# ── Thread-safe LRU cache implementation ─────────────────────────────────────
class LRUCache:
    """O(1) get/put using an OrderedDict."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache   = OrderedDict()
        self._lock    = threading.Lock()

    def get(self, key) -> object:
        with self._lock:
            if key not in self._cache:
                return -1
            self._cache.move_to_end(key)   # mark as recently used
            return self._cache[key]

    def put(self, key, value) -> None:
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
            self._cache[key] = value
            if len(self._cache) > self.capacity:
                self._cache.popitem(last=False)   # evict least recently used

    def __len__(self) -> int:
        return len(self._cache)

    def __repr__(self) -> str:
        return f"LRUCache({dict(self._cache)})"


lru = LRUCache(3)
lru.put("a", 1); lru.put("b", 2); lru.put("c", 3)
print(lru)            # {'a': 1, 'b': 2, 'c': 3}
lru.get("a")          # access 'a' → moves to end
lru.put("d", 4)       # evicts 'b' (LRU)
print(lru)            # {'c': 3, 'a': 1, 'd': 4}
print(lru.get("b"))   # -1 (evicted)


# ── TTL (time-to-live) cache ──────────────────────────────────────────────────
class TTLCache:
    def __init__(self, ttl: float):
        self._store: dict = {}    # key → (value, expires_at)
        self._ttl   = ttl
        self._lock  = threading.Lock()

    def get(self, key):
        with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            value, expires = entry
            if time.monotonic() > expires:
                del self._store[key]
                return None
            return value

    def set(self, key, value) -> None:
        with self._lock:
            self._store[key] = (value, time.monotonic() + self._ttl)

    def invalidate(self, key) -> None:
        with self._lock:
            self._store.pop(key, None)


ttl = TTLCache(ttl=0.5)
ttl.set("x", 42)
print(ttl.get("x"))     # 42
time.sleep(0.6)
print(ttl.get("x"))     # None (expired)


# ── Memoisation decorator with typed key ─────────────────────────────────────
def memoize(func):
    """Cache using the full args tuple as key (args must be hashable)."""
    _cache: dict = {}

    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]

    wrapper.cache       = _cache
    wrapper.cache_clear = lambda: _cache.clear()
    return wrapper

@memoize
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(30))
print(f"Cache size: {len(fib.cache)}")
