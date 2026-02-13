from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> None:
        ...


class QuickSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> None:
        data.sort()
        print("QuickSort applied")


class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> None:
        n = len(data)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if data[i - 1] > data[i]:
                    data[i - 1], data[i] = data[i], data[i - 1]
                    swapped = True
            n -= 1
        print("BubbleSort applied")


class Sorter:
    def __init__(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: List[int]) -> None:
        self._strategy.sort(data)


def main() -> None:
    numbers = [5, 3, 8, 1, 2]
    sorter = Sorter(BubbleSortStrategy())
    sorter.sort(numbers)
    print(numbers)

    numbers = [5, 3, 8, 1, 2]
    sorter.set_strategy(QuickSortStrategy())
    sorter.sort(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
