"""Comprehensions: list, dict, set, nested, and generator expressions."""

# ── List comprehension ────────────────────────────────────────────────────────
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
print(squares)
print(evens)

# Equivalent for-loop:
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)

# ── Dict comprehension ────────────────────────────────────────────────────────
words = ["apple", "banana", "cherry"]
lengths = {w: len(w) for w in words}
print(lengths)

# Invert a dict (assumes unique values)
inv = {v: k for k, v in {"a": 1, "b": 2, "c": 3}.items()}
print(inv)   # {1: 'a', 2: 'b', 3: 'c'}

# ── Set comprehension ─────────────────────────────────────────────────────────
unique_lengths = {len(w) for w in words}
print(unique_lengths)

# ── Nested comprehension ──────────────────────────────────────────────────────
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Flatten
flat = [x for row in matrix for x in row]
print(flat)                     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)

# All pairs where a != b
pairs = [(a, b) for a in range(3) for b in range(3) if a != b]
print(pairs)

# ── Walrus operator (:=) in comprehension — Python 3.8+ ──────────────────────
import math
values = [0, 1, -1, 4, -4, 9]
# Compute sqrt only for non-negative, reuse the computed value
roots = [r for x in values if (r := math.sqrt(x)) >= 0] if False else \
        [math.sqrt(x) for x in values if x >= 0]
print(roots)

# Walrus example (avoids double computation):
data = [1, 4, -1, 9, 16, -2, 25]
filtered = [y for x in data if (y := x**0.5 if x >= 0 else None) is not None]
print(filtered)

# ── Generator expressions ─────────────────────────────────────────────────────
# Lazy: values produced one at a time — O(1) memory
gen = (x**2 for x in range(1_000_000))
print(next(gen))   # 0
print(next(gen))   # 1

# Sum using generator expression (never builds a list)
total = sum(x**2 for x in range(10_000))
print(total)

# any/all with generator expressions (short-circuit)
print(any(x > 5 for x in range(10)))     # True
print(all(x >= 0 for x in range(10)))    # True

# ── Conditional expression (ternary) ─────────────────────────────────────────
sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(sign(-5), sign(0), sign(3))
