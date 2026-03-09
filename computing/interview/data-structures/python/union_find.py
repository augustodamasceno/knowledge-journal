# Union-Find (Disjoint Set Union) with path compression + union by rank
# Both find() and union() are O(α(n)) ≈ O(1) amortised


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        """Path compression — O(α(n))."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        """Union by rank. Returns False if already in the same component."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False   # already connected
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# ---- Connected components ----
# Graph:  0--1--2    3--4
uf = UnionFind(5)
uf.unite(0, 1)
uf.unite(1, 2)
uf.unite(3, 4)

print("Components:", uf.components)              # 2
print("0 connected to 2:", uf.connected(0, 2))   # True
print("0 connected to 3:", uf.connected(0, 3))   # False

uf.unite(2, 3)
print("After connecting 2-3, components:", uf.components)  # 1

# ---- Cycle detection ----
uf2 = UnionFind(4)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
has_cycle = False
for u, v in edges:
    if not uf2.unite(u, v):
        has_cycle = True
        break
print("\nCycle detected:", has_cycle)   # True

# ---- Kruskal's MST (minimum spanning tree) sketch ----
# Sort edges by weight, greedily add if they connect different components.
weighted_edges = [(1, 0, 1), (2, 1, 2), (3, 0, 3), (4, 2, 3), (5, 1, 3)]
weighted_edges.sort()   # sort by weight
uf3 = UnionFind(4)
mst_cost, mst_edges = 0, []
for weight, u, v in weighted_edges:
    if uf3.unite(u, v):
        mst_cost += weight
        mst_edges.append((u, v, weight))

print("\nMST edges:", mst_edges)
print("MST cost:", mst_cost)
