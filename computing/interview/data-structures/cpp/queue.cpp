// Queue & Deque — std::queue (FIFO) and std::deque (double-ended)
#include <deque>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

// Classic use-case: BFS on a simple graph
void bfs(int start, const std::vector<std::vector<int>>& adj) {
    std::vector<bool> visited(adj.size(), false);
    std::queue<int> q;
    q.push(start);
    visited[start] = true;

    std::cout << "BFS order: ";
    while (!q.empty()) {
        int node = q.front(); q.pop();   // O(1)
        std::cout << node << " ";
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);        // O(1)
            }
        }
    }
    std::cout << "\n";
}

int main() {
    // --- Basic queue ---
    std::queue<int> q;
    q.push(10);   // enqueue — O(1)
    q.push(20);
    q.push(30);

    std::cout << "Front: " << q.front() << ", Back: " << q.back() << "\n";
    q.pop();   // dequeue — O(1)
    std::cout << "After dequeue, front: " << q.front() << "\n";

    // --- Deque (double-ended queue) ---
    std::deque<int> dq = {5, 6, 7};
    dq.push_front(4);   // O(1)
    dq.push_back(8);    // O(1)
    dq.pop_front();     // O(1)

    std::cout << "Deque: ";
    for (int x : dq) std::cout << x << " ";
    std::cout << "\n";

    // --- BFS demo ---
    //  0 -- 1 -- 3
    //  |    |
    //  2    4
    std::vector<std::vector<int>> adj = {
        {1, 2},    // 0
        {0, 3, 4}, // 1
        {0},       // 2
        {1},       // 3
        {1}        // 4
    };
    bfs(0, adj);

    return 0;
}
