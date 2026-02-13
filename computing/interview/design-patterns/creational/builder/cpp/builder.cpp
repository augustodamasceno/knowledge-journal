#include <iostream>
#include <string>
#include <vector>

struct Meal {
    std::vector<std::string> items;
    int calories = 0;

    void describe() const {
        std::cout << "Meal:";
        for (const auto& item : items) {
            std::cout << ' ' << item;
        }
        std::cout << " (" << calories << " kcal)\n";
    }
};

class MealBuilder {
public:
    MealBuilder& add_main(const std::string& name, int calories) {
        meal_.items.push_back(name);
        meal_.calories += calories;
        return *this;
    }

    MealBuilder& add_side(const std::string& name, int calories) {
        meal_.items.push_back(name);
        meal_.calories += calories;
        return *this;
    }

    MealBuilder& add_drink(const std::string& name, int calories) {
        meal_.items.push_back(name);
        meal_.calories += calories;
        return *this;
    }

    Meal build() {
        Meal result = meal_;
        meal_ = Meal{};
        return result;
    }

private:
    Meal meal_{};
};

class MealDirector {
public:
    Meal create_high_protein(MealBuilder& builder) {
        return builder.add_main("Grilled chicken", 400)
            .add_side("Quinoa", 180)
            .add_drink("Protein shake", 220)
            .build();
    }

    Meal create_vegetarian(MealBuilder& builder) {
        return builder.add_main("Tofu stir-fry", 320)
            .add_side("Salad", 90)
            .add_drink("Green tea", 0)
            .build();
    }
};

int main() {
    MealBuilder builder;
    MealDirector director;

    Meal protein = director.create_high_protein(builder);
    Meal veggie = director.create_vegetarian(builder);

    protein.describe();
    veggie.describe();
}
