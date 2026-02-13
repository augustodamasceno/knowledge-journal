package interview.designpatterns.creational.builder;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

final class Meal {
    private final List<String> items;
    private final int calories;

    Meal(List<String> items, int calories) {
        this.items = List.copyOf(items);
        this.calories = calories;
    }

    void describe() {
        System.out.printf("Meal: %s (%d kcal)%n", String.join(" ", items), calories);
    }
}

final class MealBuilder {
    private final List<String> items = new ArrayList<>();
    private int calories;

    MealBuilder addMain(String name, int cals) {
        items.add(name);
        calories += cals;
        return this;
    }

    MealBuilder addSide(String name, int cals) {
        items.add(name);
        calories += cals;
        return this;
    }

    MealBuilder addDrink(String name, int cals) {
        items.add(name);
        calories += cals;
        return this;
    }

    Meal build() {
        Meal meal = new Meal(items, calories);
        items.clear();
        calories = 0;
        return meal;
    }
}

final class MealDirector {
    Meal createHighProtein(MealBuilder builder) {
        return builder
            .addMain("Grilled chicken", 400)
            .addSide("Quinoa", 180)
            .addDrink("Protein shake", 220)
            .build();
    }

    Meal createVegetarian(MealBuilder builder) {
        return builder
            .addMain("Tofu stir-fry", 320)
            .addSide("Salad", 90)
            .addDrink("Green tea", 0)
            .build();
    }
}

public final class BuilderDemo {
    private BuilderDemo() {}

    public static void main(String[] args) {
        MealBuilder builder = new MealBuilder();
        MealDirector director = new MealDirector();
        director.createHighProtein(builder).describe();
        director.createVegetarian(builder).describe();
    }
}
