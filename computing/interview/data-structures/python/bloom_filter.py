# Bloom Filter — probabilistic membership testing
# False positives: possible  ("maybe in set")
# False negatives: impossible ("definitely not in set")
# Deletion: not supported in the basic version
#
# Optimal parameters:
#   m (bits) = -(n * ln(p)) / ln(2)^2
#   k (hashes) = (m/n) * ln(2)
#   where n = expected insertions, p = desired false-positive rate
import math
import mmh3        # pip install mmh3  — MurmurHash3, fast non-cryptographic hash
from bitarray import bitarray   # pip install bitarray


class BloomFilter:
    def __init__(self, n: int, fp_rate: float = 0.01):
        """
        n       : expected number of items
        fp_rate : acceptable false-positive probability (e.g. 0.01 = 1%)
        """
        self.m = self._optimal_m(n, fp_rate)
        self.k = self._optimal_k(self.m, n)
        self.bits = bitarray(self.m)
        self.bits.setall(0)

    # O(k)
    def insert(self, item: str):
        for i in range(self.k):
            idx = mmh3.hash(item, i) % self.m
            self.bits[idx] = 1

    # O(k) — False means definitely absent; True means possibly present
    def might_contain(self, item: str) -> bool:
        return all(self.bits[mmh3.hash(item, i) % self.m] for i in range(self.k))

    @staticmethod
    def _optimal_m(n: int, p: float) -> int:
        return math.ceil(-(n * math.log(p)) / (math.log(2) ** 2))

    @staticmethod
    def _optimal_k(m: int, n: int) -> int:
        return max(1, round((m / n) * math.log(2)))


# ---- Demo ----
try:
    bf = BloomFilter(n=1000, fp_rate=0.01)
    print(f"Bit array size : {bf.m}")
    print(f"Hash functions : {bf.k}")

    for word in ["apple", "banana", "cherry"]:
        bf.insert(word)

    print(f"\nmight_contain('apple'):  {bf.might_contain('apple')}")   # True
    print(f"might_contain('banana'): {bf.might_contain('banana')}")   # True
    print(f"might_contain('grape'):  {bf.might_contain('grape')}")    # False (very likely)
    print(f"might_contain('kiwi'):   {bf.might_contain('kiwi')}")     # False (very likely)

except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install mmh3 bitarray")
    print()
    # Pure-Python fallback (uses built-in hashlib)
    import hashlib

    class BloomFilterPure:
        def __init__(self, n: int, fp_rate: float = 0.01):
            self.m = math.ceil(-(n * math.log(fp_rate)) / (math.log(2) ** 2))
            self.k = max(1, round((self.m / n) * math.log(2)))
            self.bits = [False] * self.m

        def _hashes(self, item: str):
            for i in range(self.k):
                digest = hashlib.sha256(f"{item}:{i}".encode()).hexdigest()
                yield int(digest, 16) % self.m

        def insert(self, item: str):
            for idx in self._hashes(item):
                self.bits[idx] = True

        def might_contain(self, item: str) -> bool:
            return all(self.bits[idx] for idx in self._hashes(item))

    bf2 = BloomFilterPure(n=1000, fp_rate=0.01)
    for word in ["apple", "banana", "cherry"]:
        bf2.insert(word)

    print("Pure-Python fallback:")
    print(f"might_contain('apple'):  {bf2.might_contain('apple')}")
    print(f"might_contain('grape'):  {bf2.might_contain('grape')}")
