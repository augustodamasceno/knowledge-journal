#include <iostream>
#include <memory>
#include <utility>
#include <vector>

std::unique_ptr<std::vector<int>> make_samples() {
    return std::unique_ptr<std::vector<int>>(new std::vector<int>{1, 2, 3, 4});
}

int main() {
    auto owner = make_samples();
    auto borrower = std::move(owner);

    int total = 0;
    for (auto value : *borrower) {
        total += value;
    }

    auto accumulate_more = [total](int extra) mutable {
        total += extra;
        return total;
    };

    std::cout << "total: " << total << '\n';
    std::cout << "lambda result: " << accumulate_more(5) << '\n';
    std::cout << std::boolalpha << "owner still holds data? " << static_cast<bool>(owner) << '\n';
}
