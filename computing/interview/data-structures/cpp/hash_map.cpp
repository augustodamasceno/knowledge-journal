// Hash Map — using std::unordered_map (O(1) avg) and std::map (O(log n), sorted)
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <vector>

// Classic use-case: two-sum
std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen; // value -> index
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        if (seen.count(complement)) return {seen[complement], i};
        seen[nums[i]] = i;
    }
    return {};
}

int main() {
    // --- unordered_map: O(1) average ---
    std::unordered_map<std::string, int> freq;
    std::vector<std::string> words = {"apple", "banana", "apple", "cherry", "banana", "apple"};
    for (const auto& w : words) ++freq[w];

    std::cout << "Word frequencies:\n";
    for (const auto& [word, count] : freq)
        std::cout << "  " << word << ": " << count << "\n";

    // Lookup
    std::cout << "Contains 'apple': " << freq.count("apple") << "\n";
    freq.erase("banana");
    std::cout << "After erase 'banana', size: " << freq.size() << "\n";

    // --- std::map: O(log n), keys are sorted ---
    std::map<int, std::string> sorted_map = {{3, "c"}, {1, "a"}, {2, "b"}};
    std::cout << "\nSorted map (keys in order):\n";
    for (const auto& [k, v] : sorted_map)
        std::cout << "  " << k << " -> " << v << "\n";

    // --- Two-sum demo ---
    std::vector<int> nums = {2, 7, 11, 15};
    auto result = twoSum(nums, 9);
    std::cout << "\nTwo-sum indices: [" << result[0] << ", " << result[1] << "]\n";

    return 0;
}
