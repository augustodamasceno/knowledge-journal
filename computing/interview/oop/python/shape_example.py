from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing import List


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def describe(self) -> None:
        ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius * self._radius

    def describe(self) -> None:
        print(f"Circle radius={self._radius} area={self.area():.3f}")


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def describe(self) -> None:
        print(f"Rectangle {self._width}x{self._height} area={self.area():.3f}")


def main() -> None:
    shapes: List[Shape] = [Circle(2.0), Rectangle(3.0, 4.0)]
    for shape in shapes:
        shape.describe()


if __name__ == "__main__":
    main()
