from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Meal:
    items: List[str]
    calories: int

    def describe(self) -> None:
        joined = " ".join(self.items)
        print(f"Meal: {joined} ({self.calories} kcal)")


class MealBuilder:
    def __init__(self) -> None:
        self._items: List[str] = []
        self._calories = 0

    def add_main(self, name: str, calories: int) -> "MealBuilder":
        self._items.append(name)
        self._calories += calories
        return self

    def add_side(self, name: str, calories: int) -> "MealBuilder":
        self._items.append(name)
        self._calories += calories
        return self

    def add_drink(self, name: str, calories: int) -> "MealBuilder":
        self._items.append(name)
        self._calories += calories
        return self

    def build(self) -> Meal:
        meal = Meal(list(self._items), self._calories)
        self._items.clear()
        self._calories = 0
        return meal


class MealDirector:
    def create_high_protein(self, builder: MealBuilder) -> Meal:
        return (
            builder.add_main("Grilled chicken", 400)
            .add_side("Quinoa", 180)
            .add_drink("Protein shake", 220)
            .build()
        )

    def create_vegetarian(self, builder: MealBuilder) -> Meal:
        return (
            builder.add_main("Tofu stir-fry", 320)
            .add_side("Salad", 90)
            .add_drink("Green tea", 0)
            .build()
        )


def main() -> None:
    builder = MealBuilder()
    director = MealDirector()
    director.create_high_protein(builder).describe()
    director.create_vegetarian(builder).describe()


if __name__ == "__main__":
    main()
