// Segment Tree — range sum queries + point updates in O(log n)
#include <iostream>
#include <vector>

class SegmentTree {
public:
    explicit SegmentTree(const std::vector<int>& arr) : n(arr.size()), tree(4 * arr.size()) {
        build(arr, 1, 0, n - 1);
    }

    // Point update: set arr[idx] = val — O(log n)
    void update(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }

    // Range sum query: sum of arr[l..r] — O(log n)
    int query(int l, int r) const {
        return query(1, 0, n - 1, l, r);
    }

private:
    int n;
    std::vector<int> tree;

    void build(const std::vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        build(arr, 2 * node,     start,   mid);
        build(arr, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node,     start,   mid, idx, val);
        else            update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }

    int query(int node, int start, int end, int l, int r) const {
        if (r < start || end < l) return 0;           // out of range
        if (l <= start && end <= r) return tree[node]; // fully inside
        int mid = (start + end) / 2;
        return query(2 * node,     start,   mid, l, r)
             + query(2 * node + 1, mid + 1, end, l, r);
    }
};

int main() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11};
    SegmentTree st(arr);

    std::cout << "Sum [1, 3]: " << st.query(1, 3) << "\n";  // 3+5+7 = 15
    std::cout << "Sum [0, 5]: " << st.query(0, 5) << "\n";  // 36

    st.update(1, 10);   // arr[1] = 10
    std::cout << "After update arr[1]=10:\n";
    std::cout << "Sum [1, 3]: " << st.query(1, 3) << "\n";  // 10+5+7 = 22
    std::cout << "Sum [0, 2]: " << st.query(0, 2) << "\n";  // 1+10+5 = 16

    return 0;
}
