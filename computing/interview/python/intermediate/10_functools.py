"""functools: lru_cache, partial, reduce, wraps, total_ordering, singledispatch."""
from functools import (
    lru_cache, cache, partial, reduce, wraps,
    total_ordering, singledispatch
)
import operator


# ── lru_cache / cache ─────────────────────────────────────────────────────────
@lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(12)])
print(fib.cache_info())    # CacheInfo(hits=..., misses=..., maxsize=128, currsize=...)
fib.cache_clear()

# cache (Python 3.9+): unbounded, no maxsize overhead
@cache
def binomial(n: int, k: int) -> int:
    if k == 0 or k == n: return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

print(binomial(10, 3))   # 120


# ── partial ───────────────────────────────────────────────────────────────────
def power(base: float, exponent: float) -> float:
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(square(5))   # 25.0
print(cube(3))     # 27.0

# Useful with map / sorted
from functools import partial
is_divisible_by = partial(lambda div, n: n % div == 0)
# Actually:
def make_divisible_check(div):
    return partial(lambda n, d: n % d == 0, d=div)

evens = list(filter(lambda n: n % 2 == 0, range(10)))
print(evens)


# ── reduce ────────────────────────────────────────────────────────────────────
nums = [1, 2, 3, 4, 5]
print(reduce(operator.add, nums))         # 15  (sum)
print(reduce(operator.mul, nums))         # 120 (product)
print(reduce(operator.mul, nums, 10))     # 1200 (initial value 10)

# Running maximum
print(reduce(max, [3, 1, 4, 1, 5, 9, 2]))  # 9

# Flatten with reduce
nested = [[1, 2], [3, 4], [5]]
print(reduce(operator.iadd, nested, []))    # [1, 2, 3, 4, 5]


# ── wraps ─────────────────────────────────────────────────────────────────────
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def hello(name: str) -> str:
    """Say hello."""
    return f"Hello, {name}!"

print(hello.__name__)   # hello   (not 'wrapper')
print(hello.__doc__)    # Say hello.


# ── total_ordering ────────────────────────────────────────────────────────────
@total_ordering
class Version:
    def __init__(self, major: int, minor: int, patch: int):
        self.major, self.minor, self.patch = major, minor, patch

    def as_tuple(self):
        return (self.major, self.minor, self.patch)

    def __eq__(self, other) -> bool:
        return self.as_tuple() == other.as_tuple()

    def __lt__(self, other) -> bool:
        return self.as_tuple() < other.as_tuple()

    def __repr__(self) -> str:
        return f"v{self.major}.{self.minor}.{self.patch}"

versions = [Version(1, 10, 0), Version(2, 0, 0), Version(1, 2, 3)]
print(sorted(versions))   # [v1.2.3, v1.10.0, v2.0.0]


# ── singledispatch ────────────────────────────────────────────────────────────
@singledispatch
def process(value):
    raise TypeError(f"Unsupported type: {type(value).__name__}")

@process.register(int)
def _(value: int) -> str:
    return f"Integer: {value}"

@process.register(str)
def _(value: str) -> str:
    return f"String of length {len(value)}: {value!r}"

@process.register(list)
def _(value: list) -> str:
    return f"List with {len(value)} items"

print(process(42))
print(process("hello"))
print(process([1, 2, 3]))
# process(3.14)   # TypeError
