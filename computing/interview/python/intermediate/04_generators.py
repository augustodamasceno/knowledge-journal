"""Generators: yield, send, yield from, and generator pipelines."""
import itertools


# ── Basic generator ───────────────────────────────────────────────────────────
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen  = fibonacci()
first_10 = [next(gen) for _ in range(10)]
print(first_10)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ── Finite generator: reading a file in chunks ───────────────────────────────
def read_chunks(path: str, size: int = 1024):
    with open(path, "rb") as f:
        while chunk := f.read(size):
            yield chunk

# ── Generator expression ──────────────────────────────────────────────────────
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(list(even_squares))   # [0, 4, 16, 36, 64]

# ── Generator pipeline ────────────────────────────────────────────────────────
def integers(start: int = 0):
    while True:
        yield start
        start += 1

def evens(source):
    for n in source:
        if n % 2 == 0:
            yield n

def squared(source):
    for n in source:
        yield n ** 2

nums = integers()
pipeline = squared(evens(nums))
print([next(pipeline) for _ in range(5)])   # [0, 4, 16, 36, 64]

# ── yield from — delegate to sub-generator ───────────────────────────────────
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recursive delegation
        else:
            yield item

print(list(flatten([1, [2, [3, 4], 5], [6, 7]])))  # [1, 2, 3, 4, 5, 6, 7]

# yield from also passes return value
def sub():
    yield 1
    yield 2
    return "done"

def main():
    result = yield from sub()
    print(f"Sub returned: {result}")     # Sub returned: done
    yield 3

print(list(main()))   # [1, 2, 3]

# ── send() — two-way coroutine ────────────────────────────────────────────────
def running_average():
    total, count = 0.0, 0
    avg = None
    while True:
        value = yield avg     # yield sends avg out; receives next value
        if value is None:
            break
        total += value
        count += 1
        avg = total / count

ra = running_average()
next(ra)           # prime (advance to first yield)
print(ra.send(10))  # 10.0
print(ra.send(20))  # 15.0
print(ra.send(30))  # 20.0

# ── throw() and close() ───────────────────────────────────────────────────────
def gen_with_cleanup():
    try:
        while True:
            yield
    except GeneratorExit:
        print("Generator closed cleanly")
    except ValueError as e:
        print(f"Generator got ValueError: {e}")
        yield "recovered"

g = gen_with_cleanup()
next(g)
next(g.throw(ValueError("oops")), None)   # "Generator got ValueError: oops"
g.close()

# ── itertools generators ──────────────────────────────────────────────────────
# cycle: repeat an iterable forever
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week_cycle = itertools.cycle(days)
print([next(week_cycle) for _ in range(9)])

# repeat: emit a value n times (or forever)
print(list(itertools.repeat("x", 4)))   # ['x', 'x', 'x', 'x']

# count: infinite arithmetic sequence
counter = itertools.count(start=10, step=5)
print([next(counter) for _ in range(5)])   # [10, 15, 20, 25, 30]

# takewhile / dropwhile
print(list(itertools.takewhile(lambda x: x < 5, range(10))))  # [0, 1, 2, 3, 4]
print(list(itertools.dropwhile(lambda x: x < 5, range(10))))  # [5, 6, 7, 8, 9]
