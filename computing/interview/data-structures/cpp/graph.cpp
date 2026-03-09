// Graph — adjacency list representation with BFS and DFS
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Graph {
public:
    explicit Graph(int vertices) : V(vertices), adj(vertices) {}

    void addEdge(int u, int v, bool directed = false) {
        adj[u].push_back(v);
        if (!directed) adj[v].push_back(u);
    }

    // Breadth-First Search — shortest path in unweighted graph
    void bfs(int start) const {
        std::vector<bool> visited(V, false);
        std::queue<int> q;
        q.push(start);
        visited[start] = true;

        std::cout << "BFS from " << start << ": ";
        while (!q.empty()) {
            int node = q.front(); q.pop();
            std::cout << node << " ";
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        std::cout << "\n";
    }

    // Depth-First Search (iterative)
    void dfs(int start) const {
        std::vector<bool> visited(V, false);
        std::stack<int> st;
        st.push(start);

        std::cout << "DFS from " << start << ": ";
        while (!st.empty()) {
            int node = st.top(); st.pop();
            if (visited[node]) continue;
            visited[node] = true;
            std::cout << node << " ";
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) st.push(neighbor);
            }
        }
        std::cout << "\n";
    }

    // Detect cycle in undirected graph using DFS
    bool hasCycle() const {
        std::vector<bool> visited(V, false);
        for (int i = 0; i < V; ++i) {
            if (!visited[i] && dfsCycle(i, -1, visited)) return true;
        }
        return false;
    }

private:
    int V;
    std::vector<std::vector<int>> adj;

    bool dfsCycle(int node, int parent, std::vector<bool>& visited) const {
        visited[node] = true;
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                if (dfsCycle(neighbor, node, visited)) return true;
            } else if (neighbor != parent) {
                return true; // back edge
            }
        }
        return false;
    }
};

int main() {
    //  0 --- 1 --- 3
    //  |     |
    //  2     4
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);

    g.bfs(0);
    g.dfs(0);
    std::cout << std::boolalpha << "Has cycle: " << g.hasCycle() << "\n";

    Graph cyclic(3);
    cyclic.addEdge(0, 1);
    cyclic.addEdge(1, 2);
    cyclic.addEdge(2, 0);
    std::cout << "Cyclic graph has cycle: " << cyclic.hasCycle() << "\n";

    return 0;
}
