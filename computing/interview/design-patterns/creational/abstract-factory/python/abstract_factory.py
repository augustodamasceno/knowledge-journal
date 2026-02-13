from __future__ import annotations
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        ...


class Checkbox(ABC):
    @abstractmethod
    def toggle(self) -> None:
        ...


class GuiFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        ...


class WindowsButton(Button):
    def render(self) -> None:
        print("Rendering Windows button")


class WindowsCheckbox(Checkbox):
    def toggle(self) -> None:
        print("Toggling Windows checkbox")


class WindowsFactory(GuiFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacButton(Button):
    def render(self) -> None:
        print("Rendering macOS button")


class MacCheckbox(Checkbox):
    def toggle(self) -> None:
        print("Toggling macOS checkbox")


class MacFactory(GuiFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GuiFactory) -> None:
        self._factory = factory

    def paint_ui(self) -> None:
        button = self._factory.create_button()
        checkbox = self._factory.create_checkbox()
        button.render()
        checkbox.toggle()


def main() -> None:
    Application(WindowsFactory()).paint_ui()
    Application(MacFactory()).paint_ui()


if __name__ == "__main__":
    main()
