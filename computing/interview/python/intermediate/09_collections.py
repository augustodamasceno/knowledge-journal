"""The collections module: defaultdict, Counter, deque, namedtuple, ChainMap, OrderedDict."""
from collections import (
    defaultdict, Counter, deque, namedtuple, ChainMap, OrderedDict
)


# ── defaultdict ───────────────────────────────────────────────────────────────
# Groups words by their first letter
words = "the quick brown fox jumps over the lazy dog".split()
by_letter: defaultdict[str, list] = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
print(dict(by_letter))

# Word frequency with int default (default 0)
freq: defaultdict[str, int] = defaultdict(int)
for w in words:
    freq[w] += 1
print(dict(freq))

# Nested defaultdict for adjacency list
graph: defaultdict = defaultdict(lambda: defaultdict(int))
edges = [("A", "B", 3), ("A", "C", 1), ("B", "C", 2)]
for u, v, w in edges:
    graph[u][v] = w
    graph[v][u] = w
print(dict(graph))


# ── Counter ───────────────────────────────────────────────────────────────────
c = Counter("abracadabra")
print(c)                        # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c.most_common(3))         # [('a', 5), ('b', 2), ('r', 2)]
print(c["z"])                   # 0 — missing keys return 0

# Arithmetic on Counters
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)   # Counter({'a': 4, 'b': 3})
print(c1 - c2)   # Counter({'a': 2})    (drops zero / negative)
print(c1 & c2)   # min:  Counter({'a': 1, 'b': 1})
print(c1 | c2)   # max:  Counter({'a': 3, 'b': 2})

# Subtract without dropping negatives
c1.subtract(c2)
print(c1)   # Counter({'a': 2, 'b': -1})

# Total (Python 3.10+)
c = Counter(a=5, b=2, r=2)
print(c.total())   # 9

# Anagram check using Counter
def is_anagram(a: str, b: str) -> bool:
    return Counter(a.lower()) == Counter(b.lower())

print(is_anagram("listen", "silent"))   # True


# ── deque (double-ended queue) ────────────────────────────────────────────────
dq: deque[int] = deque()
dq.append(1)         # right
dq.append(2)
dq.appendleft(0)     # left  — O(1)
print(dq)            # deque([0, 1, 2])
print(dq.popleft())  # O(1)
print(dq.pop())      # O(1)

# Bounded deque: maxlen auto-evicts oldest
log: deque[str] = deque(maxlen=3)
for i in range(6):
    log.append(f"msg-{i}")
print(log)   # deque(['msg-3', 'msg-4', 'msg-5'], maxlen=3)

# rotate
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)    # right shift by 2
print(dq)       # deque([4, 5, 1, 2, 3])
dq.rotate(-1)   # left shift
print(dq)       # deque([5, 1, 2, 3, 4])

# Sliding window using deque
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    result, window = [], deque()
    for i, n in enumerate(nums):
        while window and nums[window[-1]] < n:
            window.pop()
        window.append(i)
        if window[0] == i - k:
            window.popleft()
        if i >= k - 1:
            result.append(nums[window[0]])
    return result

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]


# ── namedtuple ────────────────────────────────────────────────────────────────
Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "r g b", defaults=(255,))  # b defaults to 255

p = Point(3, 4)
print(p.x, p.y)
print(p[0], p[1])       # still indexable
print(p._asdict())
p2 = p._replace(x=10)
print(p2)

# ── ChainMap ─────────────────────────────────────────────────────────────────
defaults = {"color": "blue", "size": "L", "verbose": False}
env_vars  = {"size": "XL"}
cli_args  = {"color": "red"}

config = ChainMap(cli_args, env_vars, defaults)
print(config["color"])    # red    (from cli_args)
print(config["size"])     # XL     (from env_vars)
print(config["verbose"])  # False  (from defaults)

# Mutations only hit the first map
config["new_opt"] = "x"
print(cli_args)   # {"color": "red", "new_opt": "x"}

# ── OrderedDict ───────────────────────────────────────────────────────────────
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("a")         # move to end
od.move_to_end("c", last=False)  # move to beginning
print(list(od.keys()))      # ['c', 'b', 'a']

# OrderedDict equality is order-sensitive (unlike plain dict)
print(OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1))  # False
print(dict(a=1, b=2)        == dict(b=2, a=1))          # True
