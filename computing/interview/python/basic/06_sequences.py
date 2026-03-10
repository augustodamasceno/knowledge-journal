"""Sequences: list, tuple, range, slicing, sorting, and packing."""

# ── List operations ───────────────────────────────────────────────────────────
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(len(lst))
print(min(lst), max(lst))
print(sum(lst))

# Slicing – O(k) where k = length of slice
print(lst[1:5])       # [1, 4, 1, 5]
print(lst[::2])       # every other element
print(lst[::-1])      # reversed copy
print(lst[-3:])       # last three elements

# Modifying
lst.append(7)         # O(1) amortised
lst.insert(0, 0)      # O(n)
lst.extend([10, 11])  # O(k)
lst.pop()             # O(1) — remove from end
lst.pop(0)            # O(n) — remove from front (use collections.deque instead)
lst.remove(4)         # O(n) — remove first occurrence of value
del lst[0]            # O(n)

# Searching
print(lst.index(5))   # first occurrence (raises ValueError if absent)
print(lst.count(5))

# Copying
shallow  = lst.copy()       # or lst[:]
import copy
deep_cp  = copy.deepcopy(lst)  # for nested structures

# ── Sorting ───────────────────────────────────────────────────────────────────
nums = [5, 2, 8, 1, 9, 3]
print(sorted(nums))                         # new list, ascending
print(sorted(nums, reverse=True))           # new list, descending
nums.sort()                                 # in-place, returns None
nums.sort(key=lambda x: -x)                 # custom key

words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)                          # by length
words.sort(key=lambda w: (len(w), w))        # multi-key: length then alpha

# timsort is stable — equal elements preserve original order
data = [(1, "b"), (2, "a"), (1, "a")]
print(sorted(data, key=lambda x: x[0]))     # [(1, 'b'), (1, 'a'), (2, 'a')]

# ── Tuple ─────────────────────────────────────────────────────────────────────
t = (1, 2, 3)
print(t + (4, 5))      # concatenation
print(t * 2)           # repetition
print(t.count(1))
print(t.index(2))      # 1

# Named tuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
print(p._asdict())          # OrderedDict or dict (3.8+)
print(p._replace(x=10))     # new namedtuple with changed field

# ── Tuple packing and unpacking ───────────────────────────────────────────────
x, y, z = (1, 2, 3)
first, *rest  = [1, 2, 3, 4, 5]
head, *middle, last = range(10)
a, (b, c) = 1, (2, 3)     # nested unpacking

# Swap without temp variable
a, b = 1, 2
a, b = b, a
print(a, b)   # 2  1

# ── Range ─────────────────────────────────────────────────────────────────────
r = range(0, 20, 3)
print(list(r))       # [0, 3, 6, 9, 12, 15, 18]
print(10 in r)       # O(1)!
print(len(r))        # 7

# ── zip and enumerate ─────────────────────────────────────────────────────────
names  = ["Alice", "Bob",   "Carol"]
scores = [88,      72,      95]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")

# ── itertools operations ──────────────────────────────────────────────────────
import itertools

# Chain multiple iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))   # [1, 2, 3, 4, 5]

# islice: lazy slice of any iterable
print(list(itertools.islice(range(100), 5, 15, 2)))  # [5, 7, 9, 11, 13]

# accumulate
print(list(itertools.accumulate([1, 2, 3, 4, 5])))           # [1, 3, 6, 10, 15]
import operator
print(list(itertools.accumulate([1, 2, 3, 4], operator.mul)))  # [1, 2, 6, 24]

# product (Cartesian product)
print(list(itertools.product("AB", repeat=2)))

# combinations / permutations
print(list(itertools.combinations("ABCD", 2)))
print(list(itertools.permutations("ABC", 2)))
