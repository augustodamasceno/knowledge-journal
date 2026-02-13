from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class DiagramNode(ABC):
    def __init__(self, label: str) -> None:
        self._label = label

    @abstractmethod
    def clone(self) -> "DiagramNode":
        ...

    @abstractmethod
    def render(self) -> None:
        ...


@dataclass
class CircleNode(DiagramNode):
    _label: str
    _radius: float

    def __init__(self, label: str, radius: float) -> None:
        super().__init__(label)
        self._radius = radius

    def clone(self) -> DiagramNode:
        return CircleNode(self._label, self._radius)

    def render(self) -> None:
        print(f"Circle({self._label}, r={self._radius})")


@dataclass
class RectangleNode(DiagramNode):
    _label: str
    _width: float
    _height: float

    def __init__(self, label: str, width: float, height: float) -> None:
        super().__init__(label)
        self._width = width
        self._height = height

    def clone(self) -> DiagramNode:
        return RectangleNode(self._label, self._width, self._height)

    def render(self) -> None:
        print(f"Rectangle({self._label}, {self._width}x{self._height})")


class PrototypeRegistry:
    def __init__(self) -> None:
        self._prototypes: dict[str, DiagramNode] = {}

    def register(self, name: str, prototype: DiagramNode) -> None:
        self._prototypes[name] = prototype

    def create(self, name: str) -> DiagramNode:
        try:
            return self._prototypes[name].clone()
        except KeyError as exc:
            raise KeyError("Prototype not found") from exc


def main() -> None:
    registry = PrototypeRegistry()
    registry.register("small_circle", CircleNode("Small", 1.0))
    registry.register("wide_rect", RectangleNode("Wide", 3.0, 1.0))

    registry.create("small_circle").render()
    registry.create("wide_rect").render()


if __name__ == "__main__":
    main()
