"""Basic Python types and their properties."""

# ── Integers ────────────────────────────────────────────────────────────────
i = 42
print(type(i))          # <class 'int'>
print(isinstance(i, int))
print(i.bit_length())   # 6

# Integer division and modulo
print(7 // 2)   # 3    (floor division)
print(7 % 2)    # 1    (modulo)
print(divmod(7, 2))  # (3, 1)

# Arbitrary precision
big = 10 ** 100     # no overflow in Python
print(big)

# ── Floats ───────────────────────────────────────────────────────────────────
f = 3.14
print(f"{f:.6f}")             # 3.140000
print(round(f, 1))            # 3.1

import math
print(math.isfinite(float("inf")))    # False
print(math.isnan(float("nan")))       # True
print(math.floor(3.7), math.ceil(3.2))  # 3  4

# Float equality pitfall
print(0.1 + 0.2 == 0.3)       # False!
print(abs(0.1 + 0.2 - 0.3) < 1e-9)   # True (use tolerance)
print(math.isclose(0.1 + 0.2, 0.3))  # True

# ── Strings ──────────────────────────────────────────────────────────────────
s = "Hello, World!"
print(len(s))
print(s.upper(), s.lower())
print(s.split(", "))
print(s.replace("World", "Python"))
print("   spaces   ".strip())
print(s.startswith("Hello"), s.endswith("!"))
print(s.find("World"))     # 7   (-1 if not found)
print("abc" * 3)           # abcabcabc
print(",".join(["a", "b", "c"]))  # a,b,c

# Encoding
raw = "café"
encoded = raw.encode("utf-8")
print(encoded)              # b'caf\xc3\xa9'
print(encoded.decode("utf-8"))

# ── Bool ─────────────────────────────────────────────────────────────────────
print(True + True)   # 2  (bool is subclass of int)
print(bool(0), bool(""), bool([]), bool(None))   # all False
print(bool(1), bool("x"), bool([0]))             # all True

# ── None ─────────────────────────────────────────────────────────────────────
x = None
print(x is None)      # canonical way to check for None
print(x is not None)

# ── Bytes ─────────────────────────────────────────────────────────────────────
b = b"\x00\x01\x02\xFF"
print(len(b))
print(b[0])           # 0  (indexing gives an int)
print(b.hex())        # 000102ff
print(bytes.fromhex("deadbeef"))

# ── Type conversions ──────────────────────────────────────────────────────────
print(int("42"))
print(int("ff", 16))   # hex string → int
print(float("3.14"))
print(str(100))
print(list("abc"))     # ['a', 'b', 'c']
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))

# ── Identity caching (CPython) ────────────────────────────────────────────────
a, b = 256, 256
print(a is b)    # True  — cached small int

a, b = 257, 257
print(a is b)    # False — not guaranteed outside of assignment

# String interning
s1, s2 = "hello", "hello"
print(s1 is s2)  # True  — simple literals are interned
