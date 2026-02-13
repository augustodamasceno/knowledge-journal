from __future__ import annotations
from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def read(self) -> str:
        ...


class FileDataSource(DataSource):
    def __init__(self, contents: str) -> None:
        self._contents = contents

    def read(self) -> str:
        return self._contents


class DataSourceDecorator(DataSource):
    def __init__(self, wrappee: DataSource) -> None:
        self._wrappee = wrappee


class EncryptionDecorator(DataSourceDecorator):
    def read(self) -> str:
        return f"<encrypted>{self._wrappee.read()}</encrypted>"


class CompressionDecorator(DataSourceDecorator):
    def read(self) -> str:
        return f"<compressed>{self._wrappee.read()}</compressed>"


def main() -> None:
    source: DataSource = FileDataSource("salaries.csv")
    secured: DataSource = CompressionDecorator(EncryptionDecorator(source))
    print(secured.read())


if __name__ == "__main__":
    main()
