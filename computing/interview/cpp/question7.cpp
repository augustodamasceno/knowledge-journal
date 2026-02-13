#include <concepts>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>

template <std::ranges::input_range R>
requires std::integral<std::ranges::range_value_t<R>>
double average(R&& range) {
    long long total = 0;
    long long count = 0;
    for (int value : range) {
        total += value;
        ++count;
    }
    return count ? static_cast<double>(total) / count : 0.0;
}

int main() {
    std::vector<int> values{1, 2, 3, 4, 5, 6};
    auto evens = values | std::ranges::views::filter([](int value) { return value % 2 == 0; });

    std::cout << "even average: " << average(evens) << '\n';
}
