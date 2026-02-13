from __future__ import annotations
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> None:
        ...


class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Vector circle radius={radius:.2f}")


class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Raster circle radius={radius:.2f}")


class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        ...


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float) -> None:
        super().__init__(renderer)
        self._radius = radius

    def draw(self) -> None:
        self._renderer.render_circle(self._radius)


def main() -> None:
    Circle(VectorRenderer(), 2.5).draw()
    Circle(RasterRenderer(), 2.5).draw()


if __name__ == "__main__":
    main()
