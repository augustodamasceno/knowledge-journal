#include <algorithm>
#include <array>
#include <iostream>
#include <span>

void normalize(std::span<float> values) {
    auto [minIt, maxIt] = std::minmax_element(values.begin(), values.end());
    const float range = *maxIt - *minIt;
    if (range == 0.0f) {
        return;
    }
    for (float& value : values) {
        value = (value - *minIt) / range;
    }
}

int main() {
    std::array<float, 5> metrics{2.0f, 4.0f, 1.0f, 5.0f, 3.0f};
    normalize(metrics);
    for (float value : metrics) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}
