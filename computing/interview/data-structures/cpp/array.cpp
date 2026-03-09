// Array — using std::vector (dynamic) and std::array (fixed-size)
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

int main() {
    // --- Fixed-size array (stack allocated) ---
    std::array<int, 5> fixed = {5, 3, 1, 4, 2};
    std::sort(fixed.begin(), fixed.end());

    std::cout << "Fixed sorted: ";
    for (int x : fixed) std::cout << x << " ";
    std::cout << "\n";

    // --- Dynamic array ---
    std::vector<int> v = {10, 20, 30};
    v.push_back(40);          // O(1) amortised
    v.insert(v.begin(), 0);   // O(n) — shifts elements
    v.erase(v.begin() + 2);   // O(n) — shifts elements

    std::cout << "Dynamic: ";
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";

    // O(1) random access
    std::cout << "Element at index 1: " << v[1] << "\n";
    std::cout << "Size: " << v.size() << ", Capacity: " << v.capacity() << "\n";

    return 0;
}
