"""Python data model: full numeric type, custom container, and operator hooks."""
import math
import operator
from functools import total_ordering


# ── Complete immutable numeric type: Rational ─────────────────────────────────
@total_ordering
class Rational:
    """Exact rational number with full numeric protocol."""

    def __init__(self, numerator: int, denominator: int = 1):
        if not isinstance(numerator,   int): raise TypeError("numerator must be int")
        if not isinstance(denominator, int): raise TypeError("denominator must be int")
        if denominator == 0:                 raise ZeroDivisionError("zero denominator")
        g    = math.gcd(abs(numerator), abs(denominator))
        sign = -1 if denominator < 0 else 1
        self.num = sign * numerator   // g
        self.den = sign * denominator // g

    # ── Display ───────────────────────────────────────────────────────────────
    def __repr__(self): return f"Rational({self.num}, {self.den})"
    def __str__(self):  return f"{self.num}" if self.den == 1 else f"{self.num}/{self.den}"
    def __format__(self, spec): return format(float(self), spec)

    # ── Arithmetic ────────────────────────────────────────────────────────────
    def __add__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den + o.num * self.den, self.den * o.den)
    def __sub__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den - o.num * self.den, self.den * o.den)
    def __mul__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.num, self.den * o.den)
    def __truediv__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den, self.den * o.num)
    def __floordiv__(self, other):
        o = self._coerce(other)
        return (self.num * o.den) // (self.den * o.num)
    def __mod__(self, other):
        o = self._coerce(other)
        return self - o * (self // o)
    def __pow__(self, exp: int):
        if exp >= 0: return Rational(self.num ** exp, self.den ** exp)
        return Rational(self.den ** (-exp), self.num ** (-exp))
    def __neg__(self):   return Rational(-self.num, self.den)
    def __pos__(self):   return self
    def __abs__(self):   return Rational(abs(self.num), self.den)

    # Reflected
    def __radd__(self, o): return self + o
    def __rsub__(self, o): return self._coerce(o) - self
    def __rmul__(self, o): return self * o
    def __rtruediv__(self, o): return self._coerce(o) / self

    # ── Comparison ────────────────────────────────────────────────────────────
    def __eq__(self, other) -> bool:
        try: o = self._coerce(other)
        except TypeError: return NotImplemented
        return self.num * o.den == o.num * self.den
    def __lt__(self, other) -> bool:
        o = self._coerce(other)
        return self.num * o.den < o.num * self.den

    # ── Conversion ────────────────────────────────────────────────────────────
    def __float__(self)  -> float: return self.num / self.den
    def __int__(self)    -> int:   return self.num // self.den
    def __bool__(self)   -> bool:  return self.num != 0
    def __complex__(self)-> complex: return complex(float(self))
    def __hash__(self)   -> int:   return hash(float(self))

    # ── Round ─────────────────────────────────────────────────────────────────
    def __round__(self, ndigits=None):
        if ndigits is None:
            return int(self + Rational(1, 2))
        factor = 10 ** ndigits
        return Rational(round(self.num * factor, 0) // self.den, factor)

    # ── Helpers ───────────────────────────────────────────────────────────────
    @classmethod
    def _coerce(cls, other) -> "Rational":
        if isinstance(other, Rational): return other
        if isinstance(other, int):      return Rational(other)
        raise TypeError(f"Cannot coerce {type(other).__name__} to Rational")


# Tests
a = Rational(1, 2)
b = Rational(1, 3)
print(a + b)           # 5/6
print(a * b)           # 1/6
print(a - b)           # 1/6
print(a / b)           # 3/2
print(a ** 3)          # 1/8
print(2 * a)           # 1
print(sorted([b, a, Rational(1, 4)]))   # [1/4, 1/3, 1/2]
print(f"{a:.6f}")      # 0.500000
print(round(Rational(7, 4)))  # 2


# ── Custom mapping type ───────────────────────────────────────────────────────
class FrozenDict:
    """Immutable, hashable dict-like container."""

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._hash  = None

    def __getitem__(self, key):   return self._data[key]
    def __len__(self):            return len(self._data)
    def __iter__(self):           return iter(self._data)
    def __contains__(self, key):  return key in self._data
    def __repr__(self):           return f"FrozenDict({self._data!r})"

    def keys(self):   return self._data.keys()
    def values(self): return self._data.values()
    def items(self):  return self._data.items()
    def get(self, key, default=None): return self._data.get(key, default)

    def __hash__(self) -> int:
        if self._hash is None:
            self._hash = hash(frozenset(self._data.items()))
        return self._hash

    def __eq__(self, other) -> bool:
        if isinstance(other, FrozenDict): return self._data == other._data
        if isinstance(other, dict):       return self._data == other
        return NotImplemented

fd = FrozenDict(a=1, b=2)
print(fd["a"])
print(hash(fd))          # stable hash
d = {fd: "value"}        # usable as dict key!
print(d[fd])
