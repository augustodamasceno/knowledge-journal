"""Type system: typing module, generics, Protocol, TypedDict, dataclasses."""
from __future__ import annotations   # deferred evaluation enables forward refs

from typing import (
    TypeVar, Generic, Protocol, runtime_checkable,
    TypedDict, Literal, Final, ClassVar, Union, Optional,
    overload, get_type_hints
)
from dataclasses import dataclass, field
import sys

T   = TypeVar("T")
K   = TypeVar("K")
V   = TypeVar("V")
Num = TypeVar("Num", int, float, complex)


# ── Generic class ─────────────────────────────────────────────────────────────
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

s: Stack[int] = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop(), s.peek())   # 3  2


# ── Generic function ──────────────────────────────────────────────────────────
def first(seq: list[T]) -> T:
    return seq[0]

def zip_map(keys: list[K], values: list[V]) -> dict[K, V]:
    return dict(zip(keys, values))

print(zip_map(["a", "b"], [1, 2]))


# ── Protocol (structural subtyping) ───────────────────────────────────────────
@runtime_checkable
class Serializable(Protocol):
    def serialize(self) -> bytes: ...

    @classmethod
    def deserialize(cls, data: bytes) -> Serializable: ...


class JsonRecord:
    def __init__(self, data: dict):
        self.data = data

    def serialize(self) -> bytes:
        import json
        return json.dumps(self.data).encode()

    @classmethod
    def deserialize(cls, data: bytes) -> JsonRecord:
        import json
        return cls(json.loads(data))


def save(obj: Serializable, path: str) -> None:
    with open(path, "wb") as f:
        f.write(obj.serialize())

rec = JsonRecord({"id": 1, "name": "Alice"})
print(isinstance(rec, Serializable))   # True (runtime_checkable)


# ── TypedDict ────────────────────────────────────────────────────────────────
class UserRecord(TypedDict):
    id:    int
    name:  str
    email: str

class PartialUser(TypedDict, total=False):   # all fields optional
    id:    int
    name:  str

def create_user(data: UserRecord) -> str:
    return f"User {data['name']} (id={data['id']})"

user: UserRecord = {"id": 1, "name": "Bob", "email": "bob@example.com"}
print(create_user(user))


# ── Literal and Final ─────────────────────────────────────────────────────────
Direction  = Literal["N", "S", "E", "W"]
MAX_RETRY:  Final[int] = 3

def move(direction: Direction, steps: int) -> str:
    return f"Moving {direction} by {steps} steps"

# Attempting MAX_RETRY = 5 would be a mypy error


# ── ClassVar ──────────────────────────────────────────────────────────────────
class Config:
    DEBUG: ClassVar[bool] = False
    def __init__(self, host: str):
        self.host = host


# ── @overload ─────────────────────────────────────────────────────────────────
@overload
def to_string(x: int) -> str: ...
@overload
def to_string(x: float) -> str: ...
@overload
def to_string(x: list) -> str: ...

def to_string(x):
    if isinstance(x, list):
        return "[" + ", ".join(str(i) for i in x) + "]"
    return str(x)

print(to_string(42))
print(to_string([1, 2, 3]))


# ── dataclass ────────────────────────────────────────────────────────────────
@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        import math
        return math.hypot(self.x - other.x, self.y - other.y)

@dataclass
class Graph:
    nodes: list[str]                  = field(default_factory=list)
    edges: dict[str, list[str]]       = field(default_factory=dict)

    def add_edge(self, u: str, v: str) -> None:
        self.edges.setdefault(u, []).append(v)


p1, p2 = Point(0, 0), Point(3, 4)
print(p1.distance_to(p2))   # 5.0
print(p1 < p2)              # True (order=True enables comparison by fields)
print(Point(3, 4) == Point(3, 4))  # True (frozen + eq)

# Print all annotations at runtime
print(get_type_hints(UserRecord))
