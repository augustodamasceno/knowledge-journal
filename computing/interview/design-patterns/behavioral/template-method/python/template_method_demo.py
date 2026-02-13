from __future__ import annotations
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self, input_text: str) -> None:
        cleaned = self.sanitize(input_text)
        transformed = self.transform(cleaned)
        self.persist(transformed)

    def sanitize(self, input_text: str) -> str:
        return "".join(input_text.split())

    @abstractmethod
    def transform(self, sanitized: str) -> str:
        ...

    @abstractmethod
    def persist(self, transformed: str) -> None:
        ...


class UppercaseProcessor(DataProcessor):
    def transform(self, sanitized: str) -> str:
        return sanitized.upper()

    def persist(self, transformed: str) -> None:
        print(f"Persisting uppercase string: {transformed}")


class HashProcessor(DataProcessor):
    def transform(self, sanitized: str) -> str:
        hash_value = 17
        for char in sanitized:
            hash_value = hash_value * 31 + ord(char)
        return str(hash_value)

    def persist(self, transformed: str) -> None:
        print(f"Persisting hash: {transformed}")


def main() -> None:
    upper = UppercaseProcessor()
    hash_processor = HashProcessor()

    upper.process("  Hello Template Method  ")
    hash_processor.process("  Hello Template Method  ")


if __name__ == "__main__":
    main()
