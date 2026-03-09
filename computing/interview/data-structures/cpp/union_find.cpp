// Union-Find (Disjoint Set Union) with path compression + union by rank
// Both find() and union() are effectively O(1) — O(α(n)) amortised
#include <iostream>
#include <numeric>
#include <vector>

class UnionFind {
public:
    explicit UnionFind(int n) : parent(n), rank(n, 0), components(n) {
        std::iota(parent.begin(), parent.end(), 0);  // parent[i] = i
    }

    // Find with path compression — O(α(n))
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);  // path compression
        return parent[x];
    }

    // Union by rank — O(α(n))
    bool unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;   // already same component

        if (rank[rx] < rank[ry]) std::swap(rx, ry);
        parent[ry] = rx;
        if (rank[rx] == rank[ry]) ++rank[rx];
        --components;
        return true;
    }

    bool connected(int x, int y) { return find(x) == find(y); }
    int  countComponents() const  { return components; }

private:
    std::vector<int> parent, rank;
    int components;
};

// Classic use-case: count connected components + cycle detection
int main() {
    // --- Connected components ---
    // Graph:  0--1--2    3--4
    UnionFind uf(5);
    uf.unite(0, 1);
    uf.unite(1, 2);
    uf.unite(3, 4);

    std::cout << "Components: " << uf.countComponents() << "\n";  // 2
    std::cout << std::boolalpha;
    std::cout << "0 connected to 2: " << uf.connected(0, 2) << "\n";  // true
    std::cout << "0 connected to 3: " << uf.connected(0, 3) << "\n";  // false

    uf.unite(2, 3);
    std::cout << "After connecting 2-3, components: " << uf.countComponents() << "\n";  // 1

    // --- Cycle detection: unite returns false if already connected ---
    UnionFind uf2(4);
    std::vector<std::pair<int,int>> edges = {{0,1},{1,2},{2,3},{3,0}};
    bool has_cycle = false;
    for (auto [u, v] : edges) {
        if (!uf2.unite(u, v)) { has_cycle = true; break; }
    }
    std::cout << "\nCycle detected: " << has_cycle << "\n";  // true

    return 0;
}
