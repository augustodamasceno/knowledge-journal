from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class TextMemento:
    state: str


class TextEditor:
    def __init__(self) -> None:
        self.content = ""

    def type(self, text: str) -> None:
        self.content += text

    def save(self) -> TextMemento:
        return TextMemento(self.content)

    def restore(self, memento: TextMemento) -> None:
        self.content = memento.state


class History:
    def __init__(self) -> None:
        self._snapshots: list[TextMemento] = []

    def push(self, memento: TextMemento) -> None:
        self._snapshots.append(memento)

    def pop(self) -> TextMemento:
        if not self._snapshots:
            raise IndexError("No states saved")
        return self._snapshots.pop()


def main() -> None:
    editor = TextEditor()
    history = History()

    editor.type("Hello")
    history.push(editor.save())

    editor.type(" World")
    print(f"Current: {editor.content}")

    editor.restore(history.pop())
    print(f"After undo: {editor.content}")


if __name__ == "__main__":
    main()
