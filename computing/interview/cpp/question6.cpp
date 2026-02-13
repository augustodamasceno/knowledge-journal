#include <iostream>
#include <memory>
#include <vector>

auto make_scaler(int factor) {
    return [factor](auto value) { return value * factor; };
}

auto make_numbers() {
    return std::make_unique<std::vector<int>>(std::initializer_list<int>{1, 3, 5});
}

int main() {
    auto numbers = make_numbers();
    auto scaler = make_scaler(4);

    auto sum = 0;
    for (auto value : *numbers) {
        sum += value;
    }

    std::cout << "sum: " << sum << '\n';
    std::cout << "scaled sum: " << scaler(sum) << '\n';
}
