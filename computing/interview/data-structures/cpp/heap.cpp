// Heap — using std::priority_queue (max-heap by default)
#include <iostream>
#include <queue>
#include <vector>
#include <functional>   // std::greater

// Classic use-case: k largest elements
std::vector<int> kLargest(std::vector<int> nums, int k) {
    // Min-heap of size k — keeps the k largest seen so far
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    for (int x : nums) {
        min_heap.push(x);
        if (static_cast<int>(min_heap.size()) > k) min_heap.pop();
    }
    std::vector<int> result;
    while (!min_heap.empty()) { result.push_back(min_heap.top()); min_heap.pop(); }
    return result;
}

int main() {
    // --- Max-heap (default) ---
    std::priority_queue<int> max_heap;
    for (int v : {3, 1, 4, 1, 5, 9, 2, 6}) max_heap.push(v);  // O(log n) each

    std::cout << "Max-heap pop order: ";
    while (!max_heap.empty()) {
        std::cout << max_heap.top() << " ";   // O(1)
        max_heap.pop();                        // O(log n)
    }
    std::cout << "\n";

    // --- Min-heap ---
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    for (int v : {3, 1, 4, 1, 5, 9, 2, 6}) min_heap.push(v);

    std::cout << "Min-heap top (smallest): " << min_heap.top() << "\n";

    // --- k largest demo ---
    std::vector<int> nums = {7, 10, 4, 3, 20, 15};
    auto result = kLargest(nums, 3);
    std::cout << "3 largest: ";
    for (int x : result) std::cout << x << " ";
    std::cout << "\n";

    // --- Build heap from vector in O(n) ---
    std::vector<int> data = {5, 1, 8, 3, 2};
    std::priority_queue<int> heap(data.begin(), data.end());
    std::cout << "Heap from vector, max: " << heap.top() << "\n";

    return 0;
}
