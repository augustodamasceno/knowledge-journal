# Queue — collections.deque (O(1) at both ends) and queue.Queue (thread-safe)
from collections import deque
from queue import Queue


def bfs(start: int, adj: list[list[int]]) -> list[int]:
    """BFS traversal — returns visited order."""
    visited = [False] * len(adj)
    order = []
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()          # O(1)
        order.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)  # O(1)
    return order


# --- deque as FIFO queue ---
q = deque()
q.append(10)    # enqueue — O(1)
q.append(20)
q.append(30)
print("Front:", q[0])
print("Dequeued:", q.popleft())   # O(1)
print("Queue:", list(q))

# --- queue.Queue: thread-safe FIFO ---
tq: Queue[str] = Queue()
tq.put("task-A")
tq.put("task-B")
tq.put("task-C")
print("Thread-safe queue size:", tq.qsize())
print("Got:", tq.get())   # blocks if empty

# --- BFS demo ---
#  0 -- 1 -- 3
#  |    |
#  2    4
adj = [[1, 2], [0, 3, 4], [0], [1], [1]]
print("BFS from 0:", bfs(0, adj))
