# Hash Map — Python dict (built-in, O(1) avg) and collections.Counter / defaultdict
from collections import Counter, defaultdict


def two_sum(nums: list[int], target: int) -> list[int]:
    """Classic use-case: two-sum."""
    seen: dict[int, int] = {}   # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []


# --- Plain dict ---
freq: dict[str, int] = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for w in words:
    freq[w] = freq.get(w, 0) + 1       # manual frequency count

print("Frequencies:", freq)
print("Contains 'apple':", "apple" in freq)
del freq["banana"]
print("After deleting 'banana':", freq)

# --- defaultdict: no KeyError on missing keys ---
graph: defaultdict[str, list[str]] = defaultdict(list)
graph["a"].append("b")
graph["a"].append("c")
graph["b"].append("d")
print("\nDefault-dict graph:", dict(graph))

# --- Counter: frequency counter with extras ---
counter = Counter(["a", "b", "a", "c", "b", "a"])
print("\nCounter:", counter)
print("Most common 2:", counter.most_common(2))
counter.update(["b", "b"])
print("After update:", counter)

# --- Two-sum demo ---
print("\nTwo-sum([2,7,11,15], 9):", two_sum([2, 7, 11, 15], 9))
