"""Functions: defaults, *args/**kwargs, closures, and scoping."""

# ── Basic function ────────────────────────────────────────────────────────────
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", greeting="Hi"))

# ── *args and **kwargs ────────────────────────────────────────────────────────
def show(*args, **kwargs):
    print(f"args  = {args}")      # always a tuple
    print(f"kwargs= {kwargs}")    # always a dict

show(1, 2, 3, x=10, y=20)

# Forwarding everything
def wrapper(*args, **kwargs):
    return show(*args, **kwargs)

# Keyword-only (after *)
def kw_only(a, *, b, c=0):
    return a + b + c

print(kw_only(1, b=2, c=3))

# Positional-only (before /)  — Python 3.8+
def pos_only(a, b, /, c=0):
    return a + b + c

print(pos_only(1, 2, c=3))

# ── Mutable default argument pitfall ─────────────────────────────────────────
def bad_append(val, lst=[]):     # lst is shared across ALL calls!
    lst.append(val)
    return lst

print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2]  ← bug

def good_append(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

print(good_append(1))   # [1]
print(good_append(2))   # [2]  ← correct

# ── Closures ──────────────────────────────────────────────────────────────────
def make_counter(start: int = 0):
    count = start
    def increment(step: int = 1):
        nonlocal count      # access enclosing scope variable
        count += step
        return count
    return increment

counter = make_counter(10)
print(counter())    # 11
print(counter(5))   # 16

# Classic pitfall: late binding in closures
# BAD:
fns = [lambda: i for i in range(5)]
print([f() for f in fns])   # [4, 4, 4, 4, 4] — all capture same `i`

# FIX: capture by default argument
fns = [lambda i=i: i for i in range(5)]
print([f() for f in fns])   # [0, 1, 2, 3, 4]

# ── LEGB scope rule ───────────────────────────────────────────────────────────
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)        # local
    inner()
    print(x)            # enclosing

outer()
print(x)                # global

# ── First-class functions ─────────────────────────────────────────────────────
def apply(func, values):
    return [func(v) for v in values]

print(apply(abs, [-3, -1, 2, -4]))   # [3, 1, 2, 4]

# ── Annotations / type hints ──────────────────────────────────────────────────
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)   # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
