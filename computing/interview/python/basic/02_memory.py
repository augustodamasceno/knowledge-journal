"""Memory management in CPython: reference counting and GC."""
import sys
import gc

# ── Reference counting ────────────────────────────────────────────────────────
x = [1, 2, 3]
print(f"refcount after creation:       {sys.getrefcount(x)}")  # +1 for the getrefcount arg

y = x      # another reference
print(f"refcount after   y = x:        {sys.getrefcount(x)}")

del y
print(f"refcount after del y:          {sys.getrefcount(x)}")

# id() — memory address in CPython
a = "hello"
b = "hello"
print(f"id(a)={id(a)}, id(b)={id(b)}, a is b = {a is b}")  # True — interned

# ── Cyclic garbage collector ──────────────────────────────────────────────────
class Node:
    def __init__(self, val):
        self.val = val
        self.ref = None

a = Node(1)
b = Node(2)
a.ref = b    # a → b
b.ref = a    # b → a  — cycle

del a, b     # ref counts drop to 1 (not 0), so not freed by refcount
             # The GC cycle-collector will detect and free them

gc.collect()           # force a GC cycle
print(f"GC stats: {gc.get_stats()}")

# ── GC thresholds ─────────────────────────────────────────────────────────────
print(f"Thresholds: {gc.get_threshold()}")   # (700, 10, 10) by default
gc.set_threshold(1000, 10, 10)

# ── Weak references ───────────────────────────────────────────────────────────
import weakref

class Expensive:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"{self.name} destroyed")

obj  = Expensive("big_object")
weak = weakref.ref(obj)

print(f"Alive:   {weak()}")    # <Expensive ...>
del obj
import gc; gc.collect()
print(f"Dead:    {weak()}")    # None

# ── Memory size ───────────────────────────────────────────────────────────────
print(f"int   : {sys.getsizeof(0)} bytes")       # 28
print(f"float : {sys.getsizeof(0.0)} bytes")     # 24
print(f"list  : {sys.getsizeof([1,2,3])} bytes") # 88 (does not include elements)
print(f"dict  : {sys.getsizeof({})} bytes")      # 64
print(f"str   : {sys.getsizeof('')} bytes")      # 49 base
