# Graph — adjacency list with BFS, DFS, and cycle detection
from collections import deque


class Graph:
    def __init__(self, directed: bool = False):
        self.adj: dict[int, list[int]] = {}
        self.directed = directed

    def add_edge(self, u: int, v: int):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, [])
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start: int) -> list[int]:
        """Shortest path in unweighted graph."""
        visited = set()
        order = []
        q = deque([start])
        visited.add(start)
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return order

    def dfs(self, start: int) -> list[int]:
        """Iterative DFS."""
        visited = set()
        order = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for neighbor in reversed(self.adj.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
        return order

    def has_cycle_undirected(self) -> bool:
        """Cycle detection in an undirected graph using DFS."""
        visited: set[int] = set()

        def dfs_cycle(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    if dfs_cycle(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True   # back edge = cycle
            return False

        return any(
            dfs_cycle(node, -1)
            for node in self.adj
            if node not in visited
        )


# --- Demo ---
#  0 -- 1 -- 3
#  |    |
#  2    4
g = Graph()
for u, v in [(0, 1), (0, 2), (1, 3), (1, 4)]:
    g.add_edge(u, v)

print("BFS from 0:", g.bfs(0))
print("DFS from 0:", g.dfs(0))
print("Has cycle:", g.has_cycle_undirected())

cyclic = Graph()
for u, v in [(0, 1), (1, 2), (2, 0)]:
    cyclic.add_edge(u, v)
print("Cyclic graph has cycle:", cyclic.has_cycle_undirected())
