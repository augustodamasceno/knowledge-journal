from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        ...


class ModernCircle(Shape):
    def __init__(self, radius: int) -> None:
        self._radius = radius

    def draw(self) -> None:
        print(f"Drawing modern circle r={self._radius}")


class LegacyRectangle:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def old_draw(self) -> None:
        print(f"Drawing legacy rectangle at ({self._x}, {self._y}) size {self._width}x{self._height}")


class RectangleAdapter(Shape):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self._adaptee = LegacyRectangle(x, y, width, height)

    def draw(self) -> None:
        self._adaptee.old_draw()


def main() -> None:
    circle: Shape = ModernCircle(5)
    rectangle: Shape = RectangleAdapter(10, 10, 20, 15)
    circle.draw()
    rectangle.draw()


if __name__ == "__main__":
    main()
