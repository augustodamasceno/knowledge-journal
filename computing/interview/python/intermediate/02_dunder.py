"""Dunder (magic) methods: the Python data model."""
import math
from functools import total_ordering


# ── Numeric type: Fraction ────────────────────────────────────────────────────
@total_ordering   # only needs __eq__ and __lt__; derives the rest
class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be 0")
        g    = math.gcd(abs(numerator), abs(denominator))
        sign = -1 if denominator < 0 else 1
        self.num = sign * numerator   // g
        self.den = sign * denominator // g

    # ── Display ───────────────────────────────────────────────────────────────
    def __repr__(self) -> str:  return f"Fraction({self.num}, {self.den})"
    def __str__(self)  -> str:  return f"{self.num}/{self.den}"
    def __format__(self, spec)-> str:
        return format(float(self), spec)

    # ── Arithmetic ────────────────────────────────────────────────────────────
    def __add__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)
    def __sub__(self, other):
        return Fraction(self.num * other.den - other.num * self.den,
                        self.den * other.den)
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)
    def __neg__(self)  -> "Fraction": return Fraction(-self.num, self.den)
    def __abs__(self)  -> "Fraction": return Fraction(abs(self.num), self.den)
    def __pos__(self)  -> "Fraction": return Fraction(self.num, self.den)

    # Reflected arithmetic (e.g., 2 + Fraction(…))
    def __radd__(self, other: int): return self + Fraction(other)
    def __rmul__(self, other: int): return self * Fraction(other)

    # ── Comparison ────────────────────────────────────────────────────────────
    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.den == other.num * self.den
    def __lt__(self, other) -> bool:
        return self.num * other.den <  other.num * self.den

    # ── Conversion ────────────────────────────────────────────────────────────
    def __float__(self) -> float: return self.num / self.den
    def __int__(self)   -> int:   return self.num // self.den
    def __bool__(self)  -> bool:  return self.num != 0
    def __hash__(self)  -> int:   return hash((self.num, self.den))


a = Fraction(1, 2)
b = Fraction(1, 3)
print(a + b)          # 5/6
print(a * b)          # 1/6
print(f"{a:.4f}")     # 0.5000
print(sorted([b, a, Fraction(1, 4)]))  # [1/4, 1/3, 1/2]

# ── Container: SortedList ────────────────────────────────────────────────────
import bisect

class SortedList:
    def __init__(self):
        self._data: list = []

    def add(self, item):
        bisect.insort(self._data, item)

    def __len__(self)        -> int:  return len(self._data)
    def __getitem__(self, i):         return self._data[i]
    def __contains__(self, item):     return bisect.bisect_left(self._data, item) < len(self._data) \
                                             and self._data[bisect.bisect_left(self._data, item)] == item
    def __iter__(self):               return iter(self._data)
    def __repr__(self)       -> str:  return f"SortedList({self._data})"

    def remove(self, item):
        i = bisect.bisect_left(self._data, item)
        if i < len(self._data) and self._data[i] == item:
            del self._data[i]
        else:
            raise ValueError(f"{item} not in list")


sl = SortedList()
for v in [5, 1, 3, 2, 4]:
    sl.add(v)
print(sl)            # SortedList([1, 2, 3, 4, 5])
print(3 in sl)       # True
sl.remove(3)
print(sl)            # SortedList([1, 2, 4, 5])

# ── Context manager protocol ──────────────────────────────────────────────────
class TempDir:
    import tempfile, shutil, os

    def __enter__(self):
        self._dir = TempDir.tempfile.mkdtemp()
        print(f"Created {self._dir}")
        return self._dir

    def __exit__(self, exc_type, exc_val, traceback):
        TempDir.shutil.rmtree(self._dir, ignore_errors=True)
        print(f"Cleaned up {self._dir}")
        return False   # don't suppress exceptions

with TempDir() as d:
    print(f"Working in {d}")
