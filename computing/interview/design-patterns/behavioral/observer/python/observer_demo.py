from __future__ import annotations
from typing import List, Protocol


class WeatherObserver(Protocol):
    def update(self, temperature: float) -> None:
        ...


class WeatherStation:
    def __init__(self) -> None:
        self._observers: List[WeatherObserver] = []
        self._temperature = 0.0

    def add_observer(self, observer: WeatherObserver) -> None:
        self._observers.append(observer)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self._notify()

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)


class DisplayPanel:
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, temperature: float) -> None:
        print(f"{self._name} temperature updated: {temperature}°C")


def main() -> None:
    station = WeatherStation()
    station.add_observer(DisplayPanel("Lobby"))
    station.add_observer(DisplayPanel("Server Room"))

    station.set_temperature(22.5)
    station.set_temperature(24.0)


if __name__ == "__main__":
    main()
