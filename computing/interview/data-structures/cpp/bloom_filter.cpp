// Bloom Filter — probabilistic membership testing
// - False positives: possible (returns "maybe in set")
// - False negatives: impossible (returns "definitely not in set")
// - No deletion in the basic version
//
// Optimal parameters:
//   bit_count  m = -(n * ln(p)) / (ln(2)^2)
//   hash count k = (m / n) * ln(2)
//   where n = expected insertions, p = desired false-positive rate
#include <bitset>
#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

class BloomFilter {
public:
    // n = expected items, fp_rate = desired false-positive probability (e.g. 0.01)
    BloomFilter(std::size_t n, double fp_rate) {
        m = static_cast<std::size_t>(
            std::ceil(-(static_cast<double>(n) * std::log(fp_rate))
                      / (std::log(2.0) * std::log(2.0))));
        k = static_cast<std::size_t>(std::round((static_cast<double>(m) / n) * std::log(2.0)));
        bits.assign(m, false);
    }

    // O(k)
    void insert(const std::string& item) {
        for (std::size_t i = 0; i < k; ++i)
            bits[hash(item, i) % m] = true;
    }

    // O(k) — returns false → definitely not present; true → possibly present
    bool mightContain(const std::string& item) const {
        for (std::size_t i = 0; i < k; ++i)
            if (!bits[hash(item, i) % m]) return false;
        return true;
    }

    std::size_t bitCount()  const { return m; }
    std::size_t hashCount() const { return k; }

private:
    std::size_t m, k;
    std::vector<bool> bits;

    // Double hashing: hash_i(x) = h1(x) + i * h2(x)
    std::size_t hash(const std::string& item, std::size_t seed) const {
        std::size_t h1 = std::hash<std::string>{}(item);
        std::size_t h2 = std::hash<std::string>{}(item + "\xff");
        return h1 + seed * h2;
    }
};

int main() {
    BloomFilter bf(1000, 0.01);  // expect 1000 items, 1% false-positive rate
    std::cout << "Bit array size:  " << bf.bitCount()  << "\n";
    std::cout << "Hash functions:  " << bf.hashCount() << "\n";

    bf.insert("apple");
    bf.insert("banana");
    bf.insert("cherry");

    std::cout << std::boolalpha;
    std::cout << "mightContain(\"apple\"):  " << bf.mightContain("apple")  << "\n";  // true
    std::cout << "mightContain(\"banana\"): " << bf.mightContain("banana") << "\n";  // true
    std::cout << "mightContain(\"grape\"):  " << bf.mightContain("grape")  << "\n";  // false (likely)
    std::cout << "mightContain(\"kiwi\"):   " << bf.mightContain("kiwi")   << "\n";  // false (likely)

    return 0;
}
