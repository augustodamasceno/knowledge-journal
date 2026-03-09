# Segment Tree — range sum queries + point updates in O(log n)


class SegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    # --- Public API ---

    def update(self, idx: int, val: int):
        """Point update: set arr[idx] = val — O(log n)."""
        self._update(1, 0, self.n - 1, idx, val)

    def query(self, l: int, r: int) -> int:
        """Range sum query: sum of arr[l..r] — O(log n)."""
        return self._query(1, 0, self.n - 1, l, r)

    # --- Internal helpers ---

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, 2 * node,     start,   mid)
        self._build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node,     start,   mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _query(self, node, start, end, l, r) -> int:
        if r < start or end < l:
            return 0                                  # out of range
        if l <= start and end <= r:
            return self.tree[node]                    # fully inside
        mid = (start + end) // 2
        return (self._query(2 * node,     start,   mid, l, r) +
                self._query(2 * node + 1, mid + 1, end, l, r))


# ---- Demo ----
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print("Sum [1, 3]:", st.query(1, 3))   # 3+5+7 = 15
print("Sum [0, 5]:", st.query(0, 5))   # 36

st.update(1, 10)   # arr[1] = 10
print("After update arr[1]=10:")
print("Sum [1, 3]:", st.query(1, 3))   # 10+5+7 = 22
print("Sum [0, 2]:", st.query(0, 2))   # 1+10+5 = 16

# ---- Range minimum with the same structure ----
class SegmentTreeMin(SegmentTree):
    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, 2 * node,     start,   mid)
        self._build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self._update(2 * node,     start,   mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def _query(self, node, start, end, l, r) -> int:
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self._query(2 * node,     start,   mid, l, r),
                   self._query(2 * node + 1, mid + 1, end, l, r))

stm = SegmentTreeMin([1, 3, 5, 7, 9, 11])
print("\nMin [1, 4]:", stm.query(1, 4))   # 3
