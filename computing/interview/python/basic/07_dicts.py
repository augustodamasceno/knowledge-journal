"""Dictionaries: internals, operations, idioms, and common patterns."""
from collections import defaultdict, OrderedDict, Counter

# ── Creation ──────────────────────────────────────────────────────────────────
d1 = {"a": 1, "b": 2}
d2 = dict(a=1, b=2)
d3 = dict(zip("abc", [1, 2, 3]))
d4 = dict.fromkeys(["x", "y", "z"], 0)
print(d1, d3, d4)

# ── Access ────────────────────────────────────────────────────────────────────
d = {"a": 1, "b": 2, "c": 3}
print(d["a"])           # KeyError if missing
print(d.get("z"))       # None (no error)
print(d.get("z", -1))  # default value

# ── Mutation ──────────────────────────────────────────────────────────────────
d["d"] = 4
d.setdefault("e", 5)    # insert only if key absent
d.update({"f": 6, "g": 7})
del d["g"]
popped = d.pop("f")     # remove and return
item   = d.popitem()    # remove and return last inserted (3.7+)

# ── Merge (Python 3.9+) ───────────────────────────────────────────────────────
merged = {"a": 1} | {"b": 2} | {"c": 3}
d |= {"z": 99}

# ── Iteration ─────────────────────────────────────────────────────────────────
for k in d:                          print(k)
for k in d.keys():                   print(k)
for v in d.values():                 print(v)
for k, v in d.items():               print(k, v)

# ── Insertion order (guaranteed 3.7+) ────────────────────────────────────────
ordered = {"c": 3, "a": 1, "b": 2}
print(list(ordered.keys()))   # ['c', 'a', 'b']

# ── Common patterns ───────────────────────────────────────────────────────────

# Frequency count
text  = "the quick brown fox jumps over the lazy dog"
freq  = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

# Equivalent — Counter
freq2 = Counter(text.split())
print(freq2.most_common(3))

# Group by key
from itertools import groupby
data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "potato")]
grouped: dict = defaultdict(list)
for category, item in data:
    grouped[category].append(item)
print(dict(grouped))

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Nested dict safe access
config = {"db": {"host": "localhost", "port": 5432}}
host = config.get("db", {}).get("host", "unknown")

# Caching / memoisation manual
memo = {}
def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print([fib(i) for i in range(10)])

# Two-sum problem (hash map approach) — O(n)
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]

# ── defaultdict ───────────────────────────────────────────────────────────────
graph: defaultdict[str, list] = defaultdict(list)
edges = [("A", "B"), ("A", "C"), ("B", "D")]
for src, dst in edges:
    graph[src].append(dst)
print(dict(graph))
