from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class FileSystemEntry(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def print(self, indent_level: int) -> None:
        ...

    def _indent(self, level: int) -> None:
        print("  " * level, end="")


class FileEntry(FileSystemEntry):
    def print(self, indent_level: int) -> None:
        self._indent(indent_level)
        print(f"File: {self._name}")


class DirectoryEntry(FileSystemEntry):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[FileSystemEntry] = []

    def add(self, entry: FileSystemEntry) -> None:
        self._children.append(entry)

    def print(self, indent_level: int) -> None:
        self._indent(indent_level)
        print(f"Dir: {self._name}")
        for child in self._children:
            child.print(indent_level + 1)


def main() -> None:
    root = DirectoryEntry("root")
    docs = DirectoryEntry("docs")
    img = FileEntry("image.png")

    docs.add(FileEntry("resume.pdf"))
    root.add(docs)
    root.add(img)

    root.print(0)


if __name__ == "__main__":
    main()
