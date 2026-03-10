"""__slots__: memory-efficient objects and attribute control."""
import sys
import tracemalloc


# ── Without __slots__ ─────────────────────────────────────────────────────────
class PointDict:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y


# ── With __slots__ ────────────────────────────────────────────────────────────
class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x, self.y = x, y


# ── Memory comparison ─────────────────────────────────────────────────────────
pd = PointDict(1.0, 2.0)
ps = PointSlots(1.0, 2.0)

print(f"PointDict  size: {sys.getsizeof(pd)} bytes (does not include __dict__)")
print(f"PointSlots size: {sys.getsizeof(ps)} bytes")

# __dict__ is a separate object
if hasattr(pd, "__dict__"):
    print(f"__dict__ overhead: {sys.getsizeof(pd.__dict__)} bytes")


# ── Bulk creation memory comparison ───────────────────────────────────────────
N = 500_000

tracemalloc.start()
dict_points = [PointDict(float(i), float(i)) for i in range(N)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"\nPointDict  peak memory for {N:,} objects: {peak / 1024**2:.1f} MB")
del dict_points

tracemalloc.start()
slot_points = [PointSlots(float(i), float(i)) for i in range(N)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"PointSlots peak memory for {N:,} objects: {peak / 1024**2:.1f} MB")
del slot_points


# ── Slots restrict attribute creation ─────────────────────────────────────────
try:
    ps.z = 3.0   # AttributeError: 'PointSlots' has no attribute 'z'
except AttributeError as e:
    print(f"\n{e}")


# ── Inheritance with __slots__ ────────────────────────────────────────────────
class Point3D(PointSlots):
    __slots__ = ("z",)   # only declare the NEW slots; inherited x, y still exist

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

p3 = Point3D(1, 2, 3)
print(p3)
print(p3.__slots__)       # ('z',) — only own slots
print(PointSlots.__slots__)  # ('x', 'y')

# If a base class has NO __slots__, the subclass will still have __dict__
class Base:
    pass   # no __slots__

class Derived(Base):
    __slots__ = ("x",)   # __dict__ still exists because Base has it

d = Derived()
d.x = 1
d.extra = 2   # allowed! because Base.__dict__ is inherited
print(hasattr(d, "__dict__"))  # True


# ── When to use __slots__ ─────────────────────────────────────────────────────
# ✔ Millions of small instances (nodes, points, records, events)
# ✔ You know the full attribute set at class definition time
# ✔ You want to prevent accidental attribute creation (stricter interface)
# ✗ You need __weakref__ support (add it explicitly to __slots__)
# ✗ You need __dict__ for dynamic attributes (don't use __slots__)
# ✗ You are using __class__ assignment with incompatible layouts

class Node:
    """Example: linked-list node benefiting from __slots__."""
    __slots__ = ("value", "next", "__weakref__")   # weakref support added

    def __init__(self, value):
        self.value = value
        self.next  = None
