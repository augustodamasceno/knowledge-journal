# Python for Interviews

A comprehensive Q&A reference from basic to expert level, with runnable code examples organised by topic.

---

## Levels

| Level | Topics |
|-------|--------|
| [Basic](#basic) | Types, control flow, functions, strings, lists, dicts, file I/O |
| [Intermediate](#intermediate) | OOP, comprehensions, iterators, generators, decorators, exceptions, modules |
| [Advanced](#advanced) | Metaclasses, descriptors, context managers, concurrency, memory model, typing |
| [Expert](#expert) | CPython internals, GIL, C extensions, async internals, metaprogramming, performance |

---

## Basic

### Q1 — What are Python's built-in data types?

| Type | Example | Mutable |
|------|---------|---------|
| `int` | `42` | No |
| `float` | `3.14` | No |
| `complex` | `2+3j` | No |
| `bool` | `True` | No |
| `str` | `"hello"` | No |
| `bytes` | `b"hi"` | No |
| `list` | `[1, 2, 3]` | Yes |
| `tuple` | `(1, 2, 3)` | No |
| `dict` | `{"a": 1}` | Yes |
| `set` | `{1, 2, 3}` | Yes |
| `frozenset` | `frozenset({1, 2})` | No |
| `NoneType` | `None` | — |

Code: [basic/01_types.py](basic/01_types.py)

---

### Q2 — How does Python manage memory?

- CPython uses **reference counting** as the primary mechanism. Every object has `ob_refcnt`; when it reaches 0, the object is deallocated immediately.
- A cyclic **garbage collector** (`gc` module) handles reference cycles (e.g., `a.ref = b; b.ref = a`).
- The **memory allocator** uses an arena/pool model for small objects (≤ 512 bytes) via `pymalloc`.
- Use `sys.getrefcount(obj)` to inspect reference count (note the call itself adds 1).
- `id(obj)` returns the memory address (CPython).

Code: [basic/02_memory.py](basic/02_memory.py)

---

### Q3 — What is the difference between `is` and `==`?

- `==` calls `__eq__` — compares **value**.
- `is` compares **identity** (same object in memory, same `id()`).
- Small integers (–5 to 256) and interned strings are cached, so `is` may return `True` unexpectedly for those.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same value
print(a is b)   # False — different objects

x = 256; y = 256
print(x is y)   # True  — CPython caches small ints

x = 257; y = 257
print(x is y)   # False in most contexts (implementation detail)
```

---

### Q4 — What are mutable vs immutable objects?

**Immutable:** `int`, `float`, `complex`, `bool`, `str`, `bytes`, `tuple`, `frozenset`.  
**Mutable:** `list`, `dict`, `set`, `bytearray`, user-defined class instances (by default).

```python
# Immutable: rebinding creates a new object
s = "hello"
s += " world"   # new str object; original "hello" is unchanged

# Mutable: modification in-place
lst = [1, 2, 3]
lst.append(4)   # same list object
```

**Gotcha — mutable default argument:**
```python
def append_to(x, lst=[]):   # lst is created ONCE at function definition
    lst.append(x)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] — NOT [2] !

# Fix:
def append_to(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
```

---

### Q5 — How do `*args` and `**kwargs` work?

```python
def func(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"extra positional: {args}")    # tuple
    print(f"extra keyword:    {kwargs}")  # dict

func(1, 2, 3, 4, x=10, y=20)
# a=1, b=2
# extra positional: (3, 4)
# extra keyword:    {'x': 10, 'y': 20}

# Keyword-only arguments (after *)
def strict(a, *, b, c=0):
    return a + b + c

strict(1, b=2)       # OK
# strict(1, 2)       # TypeError

# Positional-only arguments (before /)  — Python 3.8+
def pos_only(a, b, /, c=0):
    return a + b + c
```

Code: [basic/03_functions.py](basic/03_functions.py)

---

### Q6 — Explain list, dict, and set comprehensions.

```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
inv = {v: k for k, v in {"a": 1, "b": 2}.items()}

# Set comprehension
unique_lens = {len(w) for w in ["hi", "hello", "hey", "world"]}

# Nested comprehension (flattening a 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]

# Generator expression (lazy, no [ ])
total = sum(x**2 for x in range(1_000_000))
```

Code: [basic/04_comprehensions.py](basic/04_comprehensions.py)

---

### Q7 — How does string formatting work?

```python
name, price = "Widget", 9.99

# f-string (Python 3.6+) — preferred
print(f"{name!r} costs ${price:.2f}")

# format()
print("{} costs ${:.2f}".format(name, price))

# % operator (legacy)
print("%s costs $%.2f" % (name, price))

# f-string debug (3.8+)
value = 42
print(f"{value=}")   # value=42

# Width, alignment, fill
print(f"{'left':<10}|{'center':^10}|{'right':>10}")
print(f"{3.14159:.4f}")
print(f"{1_000_000:,}")    # 1,000,000
print(f"{255:#010b}")      # binary with width
```

Code: [basic/05_strings.py](basic/05_strings.py)

---

### Q8 — What are the main sequence operations?

```python
lst = [3, 1, 4, 1, 5, 9, 2, 6]

# Slicing [start:stop:step]
lst[1:5]      # [1, 4, 1, 5]
lst[::2]      # every other element
lst[::-1]     # reversed

# Common list methods
lst.sort()            # in-place, stable
sorted(lst)           # returns new list
lst.index(4)          # first occurrence
lst.count(1)          # number of occurrences
lst.insert(0, 0)
lst.pop()             # O(1) from end
lst.pop(0)            # O(n) from front — use deque for this

# Tuple unpacking
a, *rest, z = (1, 2, 3, 4, 5)
# a=1, rest=[2,3,4], z=5
```

Code: [basic/06_sequences.py](basic/06_sequences.py)

---

### Q9 — How do dictionaries work internally?

Python `dict` is a **hash table**:
- Keys must be **hashable** (immutable).
- Average O(1) get/set/delete; worst-case O(n) on hash collision.
- As of Python 3.7+, insertion order is **guaranteed**.
- `dict` uses open addressing with a compact array layout.

```python
d = {"a": 1, "b": 2, "c": 3}

d.get("z", 0)              # safe lookup with default
d.setdefault("d", 4)       # insert if absent
d.update({"e": 5})         

# Merge operator (3.9+)
merged = {"x": 1} | {"y": 2}
d |= {"z": 9}

# Iterating
for k, v in d.items(): ...
for k in d.keys():    ...
for v in d.values():  ...

# dict.fromkeys
zeros = dict.fromkeys(["a", "b", "c"], 0)
```

Code: [basic/07_dicts.py](basic/07_dicts.py)

---

### Q10 — How does exception handling work?

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or value error: {e}")
else:
    print("No exception occurred")   # runs only if no exception
finally:
    print("Always runs")             # cleanup

# Raising
def validate(age):
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age must be non-negative, got {age}")

# Exception chaining
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Conversion failed") from e

# Custom exception
class InsufficientFundsError(ValueError):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw {amount}; balance is {balance}")
        self.amount = amount
        self.balance = balance
```

Code: [basic/08_exceptions.py](basic/08_exceptions.py)

---

## Intermediate

### Q11 — What are the pillars of OOP in Python?

**Encapsulation, Inheritance, Polymorphism, Abstraction.**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self):
        return f"{type(self).__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius        # "protected" by convention

    @property
    def radius(self): return self._radius

    @radius.setter
    def radius(self, v):
        if v <= 0: raise ValueError("radius must be positive")
        self._radius = v

    def area(self):      return 3.14159 * self._radius ** 2
    def perimeter(self): return 2 * 3.14159 * self._radius

class Rectangle(Shape):
    def __init__(self, w, h): self._w, self._h = w, h
    def area(self):      return self._w * self._h
    def perimeter(self): return 2 * (self._w + self._h)

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.describe())    # polymorphic call
```

Code: [intermediate/01_oop.py](intermediate/01_oop.py)

---

### Q12 — What are `__dunder__` (magic) methods?

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):          return f"Vector({self.x}, {self.y})"
    def __str__(self):           return f"({self.x}, {self.y})"
    def __add__(self, other):    return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other):    return Vector(self.x-other.x, self.y-other.y)
    def __mul__(self, scalar):   return Vector(self.x*scalar, self.y*scalar)
    def __rmul__(self, scalar):  return self.__mul__(scalar)
    def __abs__(self):           return (self.x**2 + self.y**2) ** 0.5
    def __eq__(self, other):     return self.x == other.x and self.y == other.y
    def __hash__(self):          return hash((self.x, self.y))
    def __iter__(self):          return iter((self.x, self.y))
    def __getitem__(self, i):    return (self.x, self.y)[i]
    def __len__(self):           return 2
    def __bool__(self):          return self.x != 0 or self.y != 0
```

Code: [intermediate/02_dunder.py](intermediate/02_dunder.py)

---

### Q13 — What is the difference between an iterator and an iterable?

- **Iterable**: has `__iter__()` returning an iterator (e.g., `list`, `str`, `dict`).
- **Iterator**: has both `__iter__()` and `__next__()`; maintains traversal state.

```python
# Custom iterable + iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):          # makes it iterable
        return CountDownIterator(self.start)

class CountDownIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):          # iterators must also be iterable
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

for x in CountDown(5):
    print(x)

# Both in one class (common pattern)
class Range2:
    def __init__(self, stop):
        self.stop = stop
        self._i = 0

    def __iter__(self):  return self
    def __next__(self):
        if self._i >= self.stop: raise StopIteration
        self._i += 1
        return self._i - 1
```

Code: [intermediate/03_iterators.py](intermediate/03_iterators.py)

---

### Q14 — What are generators and when should you use them?

Generators are functions that `yield` values one at a time, pausing execution between calls. They are **lazy** — they produce values on demand, keeping memory usage O(1).

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
first_10 = [next(gen) for _ in range(10)]

# Generator expression
even_squares = (x**2 for x in range(100) if x % 2 == 0)

# yield from — delegate to sub-generator
def chain(*iterables):
    for it in iterables:
        yield from it

# send() — two-way communication
def accumulator():
    total = 0
    while True:
        value = yield total   # yield sends total out; receives value in
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)            # prime the generator
acc.send(10)         # 10
acc.send(20)         # 30
acc.send(5)          # 35
```

Code: [intermediate/04_generators.py](intermediate/04_generators.py)

---

### Q15 — How do decorators work?

A decorator is a callable that takes a function and returns a new function, wrapping it with additional behaviour.

```python
import functools, time

# Basic decorator
def timer(func):
    @functools.wraps(func)     # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-t0:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.1)

# Decorator with arguments
def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def connect(): ...

# Class-based decorator
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

Code: [intermediate/05_decorators.py](intermediate/05_decorators.py)

---

### Q16 — What is the difference between `@staticmethod`, `@classmethod`, and instance method?

```python
class Temperature:
    _unit = "Celsius"

    def __init__(self, degrees):
        self.degrees = degrees

    def to_fahrenheit(self):           # instance method — has self
        return self.degrees * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, f):       # class method — has cls, can access class state
        return cls((f - 32) * 5/9)

    @classmethod
    def set_unit(cls, unit):
        cls._unit = unit

    @staticmethod
    def is_valid(degrees):             # static method — no self or cls; pure utility
        return degrees >= -273.15

t = Temperature(100)
print(t.to_fahrenheit())              # 212.0
t2 = Temperature.from_fahrenheit(32) # Temperature(0)
print(Temperature.is_valid(-300))     # False
```

Code: [intermediate/06_classmethods.py](intermediate/06_classmethods.py)

---

### Q17 — How does multiple inheritance and MRO work?

Python uses the **C3 linearisation** algorithm to determine the Method Resolution Order (MRO).

```python
class A:
    def greet(self): return "A"

class B(A):
    def greet(self): return "B -> " + super().greet()

class C(A):
    def greet(self): return "C -> " + super().greet()

class D(B, C):
    def greet(self): return "D -> " + super().greet()

print(D().greet())       # D -> B -> C -> A
print(D.__mro__)
# (<class D>, <class B>, <class C>, <class A>, <class object>)

# Mixin pattern
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, msg):
        print(f"[{type(self).__name__}] {msg}")

class Service(LogMixin, JsonMixin):
    def __init__(self, name): self.name = name
```

Code: [intermediate/07_mro.py](intermediate/07_mro.py)

---

### Q18 — What are context managers and how do you write one?

Context managers implement `__enter__` / `__exit__` (or use `@contextmanager`). They guarantee setup and teardown code runs correctly even if exceptions occur.

```python
# Class-based
class ManagedFile:
    def __init__(self, path, mode="r"):
        self.path, self.mode = path, mode

    def __enter__(self):
        self.f = open(self.path, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        return False   # re-raise any exception (True would suppress it)

with ManagedFile("data.txt", "w") as f:
    f.write("hello")

# Generator-based (simpler for most cases)
from contextlib import contextmanager

@contextmanager
def timer(label=""):
    import time
    t0 = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label} elapsed: {time.perf_counter()-t0:.4f}s")

with timer("matrix multiply"):
    ...

# contextlib.suppress
from contextlib import suppress
with suppress(FileNotFoundError):
    open("nonexistent.txt")
```

Code: [intermediate/08_context_managers.py](intermediate/08_context_managers.py)

---

### Q19 — What is the `collections` module?

```python
from collections import (
    defaultdict, Counter, OrderedDict, deque, namedtuple, ChainMap
)

# defaultdict: missing key returns a default
word_index = defaultdict(list)
for i, word in enumerate("the cat sat on the mat".split()):
    word_index[word].append(i)

# Counter: multiset / frequency map
c = Counter("abracadabra")
c.most_common(3)             # [('a', 5), ('b', 2), ('r', 2)]
c + Counter("aaa")           # combine counts
c - Counter("aaa")           # subtract counts

# deque: O(1) at both ends
dq = deque(range(5), maxlen=3)   # maxlen auto-evicts oldest
dq.rotate(1)                     # shift right

# namedtuple: lightweight immutable record
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y, p._asdict())

# ChainMap: layered dict lookup
defaults = {"color": "blue", "size": "L"}
user     = {"color": "red"}
config   = ChainMap(user, defaults)
config["color"]   # "red"
config["size"]    # "L"
```

Code: [intermediate/09_collections.py](intermediate/09_collections.py)

---

### Q20 — What are `lambda`, `map`, `filter`, and `functools`?

```python
from functools import reduce, partial, lru_cache

# lambda
square = lambda x: x**2

# map / filter (return iterators)
numbers = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, numbers))
list(filter(lambda x: x % 2 == 0, numbers))

# reduce
product = reduce(lambda a, b: a * b, numbers)   # 120

# partial: freeze some arguments
def power(base, exp): return base ** exp
square  = partial(power, exp=2)
cube    = partial(power, exp=3)

# lru_cache: memoisation with max size
@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

fib.cache_info()   # CacheInfo(hits=..., misses=..., maxsize=128, currsize=...)
fib.cache_clear()
```

Code: [intermediate/10_functools.py](intermediate/10_functools.py)

---

## Advanced

### Q21 — What are descriptors?

A descriptor is an object that defines `__get__`, `__set__`, and/or `__delete__`, controlling attribute access. Properties, classmethods, and staticmethods are all implemented as descriptors.

```python
class Validated:
    """Non-data descriptor for validated numeric attributes."""
    def __set_name__(self, owner, name):
        self.name = name
        self.private = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, self.private, None)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be numeric")
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        setattr(obj, self.private, value)

class Circle:
    radius = Validated()
    def __init__(self, r): self.radius = r
    def area(self): return 3.14159 * self.radius**2

c = Circle(5)
c.radius = 10     # triggers __set__
# c.radius = -1   # ValueError
```

Code: [advanced/01_descriptors.py](advanced/01_descriptors.py)

---

### Q22 — What are metaclasses?

A metaclass is the class of a class. `type` is the default metaclass. By defining a custom metaclass you can intercept class creation and modify class objects.

```python
# type(name, bases, namespace) creates a class dynamically
Dog = type("Dog", (object,), {"speak": lambda self: "Woof"})

# Custom metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self): self.connected = False

# Auto-register subclasses
class PluginMeta(type):
    registry = {}
    def __new__(mcs, name, bases, ns):
        cls = super().__new__(mcs, name, bases, ns)
        if bases:   # skip the base class itself
            PluginMeta.registry[name] = cls
        return cls

class Plugin(metaclass=PluginMeta): ...
class AudioPlugin(Plugin): ...
class VideoPlugin(Plugin): ...

print(PluginMeta.registry)   # {'AudioPlugin': ..., 'VideoPlugin': ...}
```

Code: [advanced/02_metaclasses.py](advanced/02_metaclasses.py)

---

### Q23 — How does `async`/`await` work?

Python's `asyncio` uses a **single-threaded event loop** and cooperative multitasking. Coroutines suspend at `await` points, allowing the event loop to run other tasks.

```python
import asyncio, aiohttp, time

# Basic coroutine
async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

# Run coroutines concurrently
async def main():
    t0 = time.perf_counter()
    await asyncio.gather(
        greet("Alice", 1),
        greet("Bob",   0.5),
        greet("Carol", 0.8),
    )
    print(f"Total: {time.perf_counter()-t0:.2f}s")   # ~1s, not 2.3s

asyncio.run(main())

# Async context manager
class AsyncDB:
    async def __aenter__(self):
        await asyncio.sleep(0.01)   # simulate connect
        return self
    async def __aexit__(self, *_):
        await asyncio.sleep(0.01)   # simulate disconnect

# Async generator
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0)
        yield i

async def consume():
    async for value in async_range(5):
        print(value)

# Semaphore: limit concurrency
async def fetch(session, url, sem):
    async with sem:
        async with session.get(url) as resp:
            return await resp.json()
```

Code: [advanced/03_async.py](advanced/03_async.py)

---

### Q24 — What are the threading and multiprocessing models?

```
- threading:       I/O-bound tasks. Multiple threads share memory. GIL prevents
                   true parallelism for CPU-bound code.
- multiprocessing: CPU-bound tasks. Separate processes, separate GIL, true parallelism.
                   Higher startup cost; IPC via Queue/Pipe/shared memory.
- concurrent.futures: unified high-level API for both.
```

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import requests, math

# ThreadPoolExecutor — I/O bound (e.g., HTTP requests)
def fetch(url):
    return requests.get(url).status_code

urls = ["https://httpbin.org/delay/1"] * 5
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(fetch, urls))

# ProcessPoolExecutor — CPU bound
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

candidates = range(10_000_000, 10_000_100)
with ProcessPoolExecutor() as ex:
    primes = list(filter(None, ex.map(is_prime, candidates)))

# Thread-safe counter using Lock
import threading
class SafeCounter:
    def __init__(self):
        self._v = 0
        self._lock = threading.Lock()
    def increment(self):
        with self._lock:
            self._v += 1
    @property
    def value(self): return self._v
```

Code: [advanced/04_concurrency.py](advanced/04_concurrency.py)

---

### Q25 — How does Python's type system and `typing` module work?

```python
from typing import (
    Any, Union, Optional, Callable, TypeVar, Generic,
    Sequence, Mapping, Iterator, Awaitable
)
from collections.abc import Generator

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)

# Protocol (structural subtyping — duck typing with type checking)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(shape: Drawable) -> None:
    shape.draw()

# TypedDict (Python 3.8+)
from typing import TypedDict

class UserRecord(TypedDict):
    id:    int
    name:  str
    email: str

# Overload for multiple signatures
from typing import overload

@overload
def process(x: int) -> str: ...
@overload
def process(x: str) -> int: ...
def process(x):
    return str(x) if isinstance(x, int) else int(x)

# dataclass with type hints
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float
    tags: list[str] = field(default_factory=list, compare=False)
```

Code: [advanced/05_typing.py](advanced/05_typing.py)

---

### Q26 — What is the Global Interpreter Lock (GIL)?

- The **GIL** is a mutex in CPython that ensures only one thread executes Python bytecode at a time.
- It exists to protect CPython's reference counting from race conditions.
- **I/O-bound** tasks release the GIL while waiting (threads still help).
- **CPU-bound** tasks are bottlenecked by the GIL (use `multiprocessing` or C extensions instead).
- **Python 3.13** introduces an experimental "no-GIL" build (`--disable-gil`).

```python
import sys, threading

# Check GIL status (Python 3.13+)
# sys._is_gil_enabled()

# Demonstrate: CPU bound — threads don't speed up
import time

def cpu_work(n=10_000_000):
    x = 0
    for i in range(n): x += i
    return x

t0 = time.perf_counter()
cpu_work(); cpu_work()
serial_time = time.perf_counter() - t0

t0 = time.perf_counter()
t1 = threading.Thread(target=cpu_work)
t2 = threading.Thread(target=cpu_work)
t1.start(); t2.start()
t1.join();  t2.join()
threaded_time = time.perf_counter() - t0

print(f"Serial:  {serial_time:.2f}s")
print(f"Threaded:{threaded_time:.2f}s")  # similar or slower!
```

Code: [advanced/06_gil.py](advanced/06_gil.py)

---

### Q27 — How does `__slots__` work and when should you use it?

```python
# Without __slots__: each instance has a __dict__ (flexible but heavier ~200 bytes)
class PointDict:
    def __init__(self, x, y):
        self.x, self.y = x, y

# With __slots__: no __dict__; attributes stored in a fixed array (~60 bytes)
class PointSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

import sys
pd = PointDict(1, 2)
ps = PointSlots(1, 2)
print(sys.getsizeof(pd))  # ~48 + __dict__ overhead
print(sys.getsizeof(ps))  # smaller; no __dict__

# Useful when: creating millions of small objects (e.g., nodes in a tree)
# Drawback: cannot add new attributes dynamically; no __dict__ by default
```

Code: [advanced/07_slots.py](advanced/07_slots.py)

---

### Q28 — What is `functools.lru_cache` / `cache` and how does it work?

```python
from functools import lru_cache, cache
import sys

# lru_cache: bounded LRU cache (evicts least-recently-used when full)
@lru_cache(maxsize=128)
def expensive(n):
    return sum(range(n))

# cache (Python 3.9+): unbounded, simpler, slightly faster
@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

# Manual implementation to understand it
def make_lru(maxsize):
    from collections import OrderedDict
    cache = OrderedDict()
    def decorator(func):
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            result = func(*args)
            cache[args] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)  # evict oldest
            return result
        return wrapper
    return decorator
```

Code: [advanced/08_caching.py](advanced/08_caching.py)

---

## Expert

### Q29 — How does Python's import system work?

```
1. sys.modules check (cache): if already imported, return cached module.
2. Find the module: sys.meta_path finders (PathFinder, FrozenImporter, BuiltinImporter).
3. Load the module: create a module object, execute the module's code in its namespace.
4. Cache in sys.modules.
```

```python
import sys, importlib

# Inspect the import chain
print(sys.meta_path)        # list of finders
print(sys.path)             # directories searched

# Reload a module (for development / plugins)
import mymodule
importlib.reload(mymodule)

# Import by string name
module = importlib.import_module("json")

# Custom importer: intercept all imports
class AuditImporter:
    def find_module(self, name, path=None):
        print(f"Importing: {name}")
        return None   # None = let default finder handle it

sys.meta_path.insert(0, AuditImporter())

# Lazy imports (avoid circular imports, speed up startup)
from importlib import import_module
def _lazy_import(name):
    return import_module(name)
```

Code: [expert/01_import_system.py](expert/01_import_system.py)

---

### Q30 — How do you implement a coroutine-based event loop from scratch?

```python
import heapq, time, selectors
from collections import deque

class SimpleEventLoop:
    """Minimal event loop to illustrate asyncio internals."""
    def __init__(self):
        self._ready:   deque  = deque()
        self._scheduled: list = []   # min-heap of (timestamp, callback)
        self._selector = selectors.DefaultSelector()

    def call_soon(self, callback, *args):
        self._ready.append((callback, args))

    def call_later(self, delay, callback, *args):
        deadline = time.monotonic() + delay
        heapq.heappush(self._scheduled, (deadline, callback, args))

    def run_once(self):
        # Move due scheduled callbacks to ready queue
        now = time.monotonic()
        while self._scheduled and self._scheduled[0][0] <= now:
            _, cb, args = heapq.heappop(self._scheduled)
            self._ready.append((cb, args))

        # Run all currently ready callbacks
        n = len(self._ready)
        for _ in range(n):
            cb, args = self._ready.popleft()
            cb(*args)

    def run_until_empty(self):
        while self._ready or self._scheduled:
            self.run_once()
            if not self._ready and self._scheduled:
                # Sleep until the next scheduled callback
                time.sleep(max(0, self._scheduled[0][0] - time.monotonic()))

loop = SimpleEventLoop()
loop.call_soon(print, "immediate 1")
loop.call_later(0.1, print, "after 100ms")
loop.call_soon(print, "immediate 2")
loop.run_until_empty()
```

Code: [expert/02_event_loop.py](expert/02_event_loop.py)

---

### Q31 — How does Python's data model enable operator overloading and customisation?

```python
# Implementing a full numeric type: Fraction
import math
from functools import total_ordering

@total_ordering   # only need __eq__ + __lt__; rest are derived
class Fraction:
    def __init__(self, num, den=1):
        if den == 0: raise ZeroDivisionError
        g = math.gcd(abs(num), abs(den))
        sign = -1 if den < 0 else 1
        self.num = sign * num // g
        self.den = sign * den // g

    def __repr__(self):  return f"Fraction({self.num}, {self.den})"
    def __str__(self):   return f"{self.num}/{self.den}"
    def __add__(self, o): return Fraction(self.num*o.den + o.num*self.den, self.den*o.den)
    def __sub__(self, o): return Fraction(self.num*o.den - o.num*self.den, self.den*o.den)
    def __mul__(self, o): return Fraction(self.num*o.num, self.den*o.den)
    def __truediv__(self, o): return Fraction(self.num*o.den, self.den*o.num)
    def __neg__(self):    return Fraction(-self.num, self.den)
    def __abs__(self):    return Fraction(abs(self.num), self.den)
    def __float__(self):  return self.num / self.den
    def __int__(self):    return self.num // self.den
    def __eq__(self, o):  return self.num*o.den == o.num*self.den
    def __lt__(self, o):  return self.num*o.den <  o.num*self.den
    def __hash__(self):   return hash((self.num, self.den))
```

Code: [expert/03_data_model.py](expert/03_data_model.py)

---

### Q32 — What are common Python performance optimisation techniques?

```python
# 1. Profile first — never optimise blind
import cProfile, pstats
cProfile.run("my_function()")

# 2. Use built-in functions and comprehensions (implemented in C)
# SLOW:
result = []
for x in data:
    result.append(x**2)
# FAST:
result = [x**2 for x in data]   # or map(lambda x: x**2, data)

# 3. Local variable lookup is faster than global
import math
def fast_sin(data):
    sin = math.sin           # local reference — faster in tight loop
    return [sin(x) for x in data]

# 4. String concatenation: join, not +=
# SLOW: O(n^2) copies
s = ""
for word in words: s += word + " "
# FAST:
s = " ".join(words)

# 5. __slots__ for memory-heavy small objects (see Q27)

# 6. numpy for numerical arrays
import numpy as np
arr = np.arange(1_000_000, dtype=np.float64)
result = np.sin(arr)   # vectorised C loop — ~100× faster than Python loop

# 7. Bitwise tricks
is_even = lambda n: not (n & 1)
fast_abs = lambda n: (n ^ (n >> 63)) - (n >> 63)   # for signed 64-bit

# 8. functools.lru_cache for repeated expensive calls (see Q28)

# 9. Avoid repeated attribute lookups in hot loops
# SLOW:
for x in data: result.append(x)
# FAST:
app = result.append
for x in data: app(x)

# 10. Use generators to avoid building large intermediate lists
total = sum(x**2 for x in range(10_000_000))   # O(1) memory
```

Code: [expert/04_performance.py](expert/04_performance.py)

---

### Q33 — How do you write thread-safe and process-safe code?

```python
import threading, multiprocessing, queue

# --- Shared-memory threading primitives ---
lock  = threading.Lock()
rlock = threading.RLock()      # re-entrant: same thread can acquire multiple times
event = threading.Event()      # one-shot signal
cond  = threading.Condition()  # wait/notify pattern
sem   = threading.Semaphore(3) # limit concurrent access to N
bsem  = threading.BoundedSemaphore(3)

# Producer-Consumer with Condition
buffer, MAX = [], 5

def producer(cond, buf):
    for i in range(10):
        with cond:
            while len(buf) >= MAX:
                cond.wait()
            buf.append(i)
            print(f"Produced {i}")
            cond.notify_all()

def consumer(cond, buf):
    consumed = 0
    while consumed < 10:
        with cond:
            while not buf:
                cond.wait()
            item = buf.pop(0)
            consumed += 1
            print(f"Consumed {item}")
            cond.notify_all()

# --- Thread-safe queue (no explicit locking needed) ---
q: queue.Queue[int] = queue.Queue(maxsize=5)

# --- Multiprocessing shared state ---
mgr = multiprocessing.Manager()
shared_dict = mgr.dict()
shared_list = mgr.list()

mp_counter = multiprocessing.Value("i", 0)
mp_lock    = multiprocessing.Lock()

def safe_increment(val, lk):
    with lk:
        val.value += 1
```

Code: [expert/05_thread_safety.py](expert/05_thread_safety.py)

---

### Q34 — How does Python's `__init_subclass__` and `__class_getitem__` work?

```python
# __init_subclass__: called on the base class when a subclass is defined
class Plugin:
    _registry: dict[str, type] = {}

    def __init_subclass__(cls, name: str = "", **kwargs):
        super().__init_subclass__(**kwargs)
        key = name or cls.__name__.lower()
        Plugin._registry[key] = cls
        print(f"Registered plugin: {key}")

class PDFPlugin(Plugin, name="pdf"): ...
class CSVPlugin(Plugin, name="csv"): ...
class JSONPlugin(Plugin):            ...   # key = "jsonplugin"

print(Plugin._registry)

# __class_getitem__: enables cls[param] syntax without metaclass
class TypedList:
    def __class_getitem__(cls, item):
        # item is the type parameter (e.g., int in TypedList[int])
        class _Typed(cls):
            __item_type__ = item
            def append(self, v):
                if not isinstance(v, item):
                    raise TypeError(f"Expected {item}, got {type(v)}")
                super().append(v)
        _Typed.__name__ = f"TypedList[{item.__name__}]"
        return _Typed

IntList = TypedList[int]
il = IntList()
il.append(1)
# il.append("x")   # TypeError
```

Code: [expert/06_init_subclass.py](expert/06_init_subclass.py)

---

### Q35 — How do you write a C extension / use ctypes / cffi?

```python
# --- ctypes: call a shared library without compilation ---
import ctypes, ctypes.util

# Load libc
libc_name = ctypes.util.find_library("c")
libc = ctypes.CDLL(libc_name)

# Call strlen
libc.strlen.restype  = ctypes.c_size_t
libc.strlen.argtypes = [ctypes.c_char_p]
print(libc.strlen(b"hello"))   # 5

# --- cffi: cleaner API, works with ABI and API modes ---
from cffi import FFI
ffi = FFI()
ffi.cdef("size_t strlen(const char *s);")
C = ffi.dlopen(None)          # None = load process symbols
print(C.strlen(b"world"))     # 5

# --- Writing a C extension (sketch, requires compilation) ---
# File: myext.c
# #include <Python.h>
# static PyObject* py_add(PyObject* self, PyObject* args) {
#     long a, b;
#     if (!PyArg_ParseTuple(args, "ll", &a, &b)) return NULL;
#     return PyLong_FromLong(a + b);
# }
# static PyMethodDef methods[] = {
#     {"add", py_add, METH_VARARGS, "Add two integers"},
#     {NULL, NULL, 0, NULL}
# };
# static struct PyModuleDef module = {
#     PyModuleDef_HEAD_INIT, "myext", NULL, -1, methods
# };
# PyMODINIT_FUNC PyInit_myext(void) { return PyModule_Create(&module); }

# Build with: python setup.py build_ext --inplace
# Or use Cython / pybind11 for higher-level C++ binding
```

Code: [expert/07_c_extensions.py](expert/07_c_extensions.py)

---

## References

### Quick Learning
- [Python Official Tutorial](https://docs.python.org/3/tutorial/) — start here for basics
- [Real Python](https://realpython.com/) — practical, well-explained articles
- [Fluent Python, 2nd ed.](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) (Ramalho) — the definitive expert-level book
- [Python Tricks](https://realpython.com/products/python-tricks-book/) — bite-sized intermediate gems

### Interview Practice
- [LeetCode — Python filter](https://leetcode.com/problemset/?difficulty=EASY&topicSlugs=array&languageTags=python3) — algorithmic problems
- [Advent of Code](https://adventofcode.com/) — puzzle problems great for Python idioms
- [Python Interview Questions — InterviewBit](https://www.interviewbit.com/python-interview-questions/)

### Deep Dives
- [CPython source on GitHub](https://github.com/python/cpython)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Inside the Python GIL](https://realpython.com/python-gil/)
- [PEP 492 — async/await](https://peps.python.org/pep-0492/)
- [PEP 525 — async generators](https://peps.python.org/pep-0525/)
