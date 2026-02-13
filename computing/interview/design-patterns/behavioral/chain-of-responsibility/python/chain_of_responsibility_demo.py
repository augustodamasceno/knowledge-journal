from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class Severity(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()


@dataclass(frozen=True)
class LogRecord:
    level: Severity
    message: str


class Logger(ABC):
    def __init__(self) -> None:
        self._next: Logger | None = None

    def set_next(self, next_logger: Logger) -> None:
        self._next = next_logger

    def handle(self, record: LogRecord) -> None:
        if self._should_handle(record.level):
            self._write(record.message)
        elif self._next:
            self._next.handle(record)
        else:
            print(f"No handler for message: {record.message}")

    @abstractmethod
    def _should_handle(self, level: Severity) -> bool:
        ...

    @abstractmethod
    def _write(self, message: str) -> None:
        ...


class ConsoleLogger(Logger):
    def _should_handle(self, level: Severity) -> bool:
        return level is Severity.INFO

    def _write(self, message: str) -> None:
        print(f"Console: {message}")


class FileLogger(Logger):
    def _should_handle(self, level: Severity) -> bool:
        return level is Severity.WARNING

    def _write(self, message: str) -> None:
        print(f"File: {message}")


class AlertLogger(Logger):
    def _should_handle(self, level: Severity) -> bool:
        return level is Severity.ERROR

    def _write(self, message: str) -> None:
        print(f"Alert: {message}")


def main() -> None:
    console = ConsoleLogger()
    file = FileLogger()
    alert = AlertLogger()

    console.set_next(file)
    file.set_next(alert)

    console.handle(LogRecord(Severity.INFO, "Starting system"))
    console.handle(LogRecord(Severity.WARNING, "Disk space low"))
    console.handle(LogRecord(Severity.ERROR, "Service offline"))


if __name__ == "__main__":
    main()
