from __future__ import annotations
from abc import ABC, abstractmethod
from collections import deque


class Editor:
    def __init__(self) -> None:
        self.content = ""

    def append(self, text: str) -> None:
        self.content += text

    def remove_last(self, length: int) -> None:
        self.content = self.content[:-length] if length <= len(self.content) else ""


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...


class AppendCommand(Command):
    def __init__(self, editor: Editor, text: str) -> None:
        self._editor = editor
        self._text = text

    def execute(self) -> None:
        self._editor.append(self._text)

    def undo(self) -> None:
        self._editor.remove_last(len(self._text))


class Invoker:
    def __init__(self) -> None:
        self._history: deque[Command] = deque()

    def run_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_last(self) -> None:
        if not self._history:
            print("Nothing to undo")
            return
        command = self._history.pop()
        command.undo()


def main() -> None:
    editor = Editor()
    invoker = Invoker()

    invoker.run_command(AppendCommand(editor, "Hello"))
    invoker.run_command(AppendCommand(editor, " World"))
    print(f"Content: {editor.content}")

    invoker.undo_last()
    print(f"After undo: {editor.content}")


if __name__ == "__main__":
    main()
