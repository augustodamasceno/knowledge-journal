# Heap — heapq module (min-heap) and nlargest/nsmallest helpers
import heapq


def k_largest(nums: list[int], k: int) -> list[int]:
    """Return k largest elements using a min-heap of size k."""
    min_heap: list[int] = []
    for x in nums:
        heapq.heappush(min_heap, x)         # O(log k)
        if len(min_heap) > k:
            heapq.heappop(min_heap)          # O(log k)
    return sorted(min_heap, reverse=True)


# --- heapq is a min-heap ---
heap: list[int] = []
for v in [3, 1, 4, 1, 5, 9, 2, 6]:
    heapq.heappush(heap, v)     # O(log n)

print("Min (top):", heap[0])    # O(1) peek
print("Pop order:", [heapq.heappop(heap) for _ in range(4)])  # O(log n) each

# --- Build heap from list in O(n) ---
data = [5, 1, 8, 3, 2]
heapq.heapify(data)             # in-place, O(n)
print("After heapify, min:", data[0])

# --- Max-heap: negate values ---
max_heap: list[int] = []
for v in [3, 1, 4, 1, 5, 9, 2, 6]:
    heapq.heappush(max_heap, -v)   # push negated

print("Max (top):", -max_heap[0])  # negate back

# --- heapq helpers ---
nums = [7, 10, 4, 3, 20, 15]
print("3 largest:", heapq.nlargest(3, nums))    # O(n log k)
print("3 smallest:", heapq.nsmallest(3, nums))  # O(n log k)

# --- k largest via function ---
print("k=3 largest (manual):", k_largest(nums, 3))
