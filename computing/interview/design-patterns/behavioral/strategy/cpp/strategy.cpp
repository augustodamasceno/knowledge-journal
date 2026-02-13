#include <algorithm>
#include <iostream>
#include <memory>
#include <vector>

class SortStrategy {
public:
    virtual ~SortStrategy() = default;
    virtual void sort(std::vector<int>& data) const = 0;
};

class QuickSortStrategy : public SortStrategy {
public:
    void sort(std::vector<int>& data) const override {
        std::sort(data.begin(), data.end());
        std::cout << "QuickSort applied\n";
    }
};

class BubbleSortStrategy : public SortStrategy {
public:
    void sort(std::vector<int>& data) const override {
        bool swapped;
        do {
            swapped = false;
            for (std::size_t i = 1; i < data.size(); ++i) {
                if (data[i - 1] > data[i]) {
                    std::swap(data[i - 1], data[i]);
                    swapped = true;
                }
            }
        } while (swapped);
        std::cout << "BubbleSort applied\n";
    }
};

class Sorter {
public:
    explicit Sorter(std::unique_ptr<SortStrategy> strategy)
        : strategy_(std::move(strategy)) {}

    void set_strategy(std::unique_ptr<SortStrategy> strategy) {
        strategy_ = std::move(strategy);
    }

    void sort(std::vector<int>& data) const {
        strategy_->sort(data);
    }

private:
    std::unique_ptr<SortStrategy> strategy_;
};

void print(const std::vector<int>& data) {
    for (int value : data) {
        std::cout << value << ' ';
    }
    std::cout << '\n';
}

int main() {
    std::vector<int> numbers = {5, 3, 8, 1, 2};
    Sorter sorter(std::make_unique<BubbleSortStrategy>());
    sorter.sort(numbers);
    print(numbers);

    numbers = {5, 3, 8, 1, 2};
    sorter.set_strategy(std::make_unique<QuickSortStrategy>());
    sorter.sort(numbers);
    print(numbers);
}
