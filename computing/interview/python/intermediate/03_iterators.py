"""Iterators vs iterables, and the iteration protocol."""

# ── Manual iterator ───────────────────────────────────────────────────────────
class CountUp:
    """Iterable that produces integers from start to stop (exclusive)."""
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop  = stop

    def __iter__(self):
        return _CountUpIter(self.start, self.stop)

    def __len__(self):
        return max(0, self.stop - self.start)


class _CountUpIter:
    def __init__(self, current: int, stop: int):
        self._current = current
        self._stop    = stop

    def __iter__(self):   # iterators must be iterable (return self)
        return self

    def __next__(self) -> int:
        if self._current >= self._stop:
            raise StopIteration
        val = self._current
        self._current += 1
        return val


for x in CountUp(3, 7):
    print(x, end=" ")    # 3 4 5 6
print()

# Can iterate multiple times because CountUp returns a fresh iterator each time
cu = CountUp(0, 3)
print(list(cu))   # [0, 1, 2]
print(list(cu))   # [0, 1, 2]  ← works again

# ── Combined iterable + iterator ──────────────────────────────────────────────
class Fibonacci:
    """Iterator that emits Fibonacci numbers indefinitely."""
    def __init__(self):
        self._a, self._b = 0, 1

    def __iter__(self): return self

    def __next__(self) -> int:
        val = self._a
        self._a, self._b = self._b, self._a + self._b
        return val


fib = Fibonacci()
first_8 = [next(fib) for _ in range(8)]
print(first_8)   # [0, 1, 1, 2, 3, 5, 8, 13]

# NOTE: Fibonacci is a one-shot iterator; once exhausted it cannot restart.
# list(Fibonacci()) would run forever — always use islice with infinite iterators.
import itertools
print(list(itertools.islice(Fibonacci(), 10)))

# ── iter() with sentinel ──────────────────────────────────────────────────────
import random
# Read random values until 0 is generated
gen = iter(lambda: random.randint(0, 5), 0)
values = list(itertools.islice(gen, 20))   # cap at 20 items
print(values)

# More practical: read a file line by line until blank line
# for line in iter(f.readline, ""):
#     process(line)

# ── reversed() requires __reversed__ or __len__ + __getitem__ ─────────────────
class Countdown:
    def __init__(self, n: int):
        self._n = n

    def __len__(self):         return self._n
    def __getitem__(self, i):  return self._n - i

    # Optional explicit __reversed__ for efficiency
    def __reversed__(self):
        for i in range(self._n):
            yield i

print(list(reversed(Countdown(5))))   # [0, 1, 2, 3, 4]

# ── Chaining with itertools ───────────────────────────────────────────────────
def take(n, it):
    return list(itertools.islice(it, n))

print(take(5, itertools.chain(range(3), range(10, 15))))  # [0, 1, 2, 10, 11]
