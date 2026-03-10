"""OOP in Python: encapsulation, inheritance, polymorphism, ABC."""
from abc import ABC, abstractmethod
import math


# ── Abstract base class ───────────────────────────────────────────────────────
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return (f"{type(self).__name__}: "
                f"area={self.area():.4f}, perimeter={self.perimeter():.4f}")


# ── Concrete subclasses ───────────────────────────────────────────────────────
class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius   # "protected" by convention (single underscore)

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._w, self._h = width, height

    def area(self)      -> float: return self._w * self._h
    def perimeter(self) -> float: return 2 * (self._w + self._h)
    def __repr__(self)  -> str:   return f"Rectangle({self._w}, {self._h})"


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f"Square({self._w})"


# ── Polymorphism ──────────────────────────────────────────────────────────────
shapes: list[Shape] = [Circle(5), Rectangle(4, 6), Square(3)]
for s in shapes:
    print(s.describe())     # each calls its own area/perimeter

# ── Class and static methods ──────────────────────────────────────────────────
class Temperature:
    _unit: str = "Celsius"

    def __init__(self, degrees: float):
        self.degrees = degrees

    def to_fahrenheit(self) -> float:
        return self.degrees * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)

    @classmethod
    def set_unit(cls, unit: str) -> None:
        cls._unit = unit

    @staticmethod
    def is_valid(degrees: float) -> bool:
        return degrees >= -273.15

    def __repr__(self) -> str:
        return f"Temperature({self.degrees:.2f} {Temperature._unit})"


t = Temperature(100)
print(t.to_fahrenheit())              # 212.0
t2 = Temperature.from_fahrenheit(32)
print(t2)                             # Temperature(0.00 Celsius)
print(Temperature.is_valid(-500))     # False

# ── Dataclass alternative ──────────────────────────────────────────────────────
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))   # 5.0
print(p2)                    # Point(x=3, y=4)
