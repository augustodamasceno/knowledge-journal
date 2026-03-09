# Data Structures for Interviews

A concise reference for the data structures most commonly tested in technical interviews. Each entry links to a working code example in C++ (STL) and Python (built-ins / standard library).

---

## Data Structures

| # | Structure | Best for | Avg. Access | Avg. Search | Avg. Insert | Avg. Delete |
|---|-----------|----------|-------------|-------------|-------------|-------------|
| 1 | [Array](#1-array) | Random access, cache-friendly iteration | O(1) | O(n) | O(n) | O(n) |
| 2 | [Linked List](#2-linked-list) | Frequent insertion/deletion at head/tail | O(n) | O(n) | O(1) | O(1) |
| 3 | [Stack](#3-stack) | LIFO — undo, DFS, expression parsing | O(n) | O(n) | O(1) | O(1) |
| 4 | [Queue / Deque](#4-queue--deque) | FIFO / sliding window, task scheduling | O(n) | O(n) | O(1) | O(1) |
| 5 | [Hash Map / Hash Set](#5-hash-map--hash-set) | Key-value lookup, frequency counting | O(1) | O(1) | O(1) | O(1) |
| 6 | [BST / AVL / Red-Black Tree](#6-bst--avl--red-black-tree) | Sorted data, range queries | O(log n) | O(log n) | O(log n) | O(log n) |
| 7 | [Heap](#7-heap) | Priority queues, k-th largest/smallest | — | O(n) | O(log n) | O(log n) |
| 8 | [Graph](#8-graph) | Networks, paths, connectivity | — | O(V+E) | O(1) | O(E) |
| 9 | [Trie](#9-trie) | Prefix search, autocomplete, word sets | O(m) | O(m) | O(m) | O(m) |
| 10 | [Union-Find (Disjoint Set)](#10-union-find-disjoint-set) | Connected components, cycle detection | — | O(α(n)) | O(α(n)) | — |
| 11 | [Segment Tree](#11-segment-tree) | Range queries + point updates | — | O(log n) | O(log n) | O(log n) |
| 12 | [Bloom Filter](#12-bloom-filter) | Probabilistic membership test | — | O(k) | O(k) | — |

> Complexities are average-case. m = key length, V = vertices, E = edges, k = number of hash functions, α = inverse Ackermann (practically constant).

---

### 1. Array

A contiguous block of memory storing elements of the same type. Direct index access in O(1). Resizable arrays (`vector` / Python `list`) amortise appends to O(1).

**When to use:** when you need fast random access or cache-friendly sequential scans.  
**Watch out for:** insertion/deletion in the middle is O(n) due to shifting.

Examples: [C++](cpp/array.cpp) · [Python](python/array.py)

---

### 2. Linked List

Nodes linked by pointers; no contiguous memory required. Singly-linked for simple traversal, doubly-linked for O(1) removal given a node pointer.

**When to use:** frequent insertion/deletion at head or tail without random access.  
**Watch out for:** no O(1) random access; extra memory per node for pointers.

Examples: [C++](cpp/linked_list.cpp) · [Python](python/linked_list.py)

---

### 3. Stack

LIFO container — push/pop at the same end. Implemented over a dynamic array or linked list.

**When to use:** recursion simulation, DFS, balanced-parentheses, monotonic-stack problems.  
**Watch out for:** stack overflow if used for deep recursion.

Examples: [C++](cpp/stack.cpp) · [Python](python/stack.py)

---

### 4. Queue / Deque

FIFO container — enqueue at the back, dequeue at the front. A **deque** (double-ended queue) supports O(1) push/pop at both ends, making it ideal for sliding-window problems.

**When to use:** BFS, sliding-window maximum/minimum, monotonic-deque problems, task scheduling.  
**Watch out for:** plain array-based queue wastes space; prefer a circular buffer or `std::deque`/`collections.deque`.

Examples: [C++](cpp/queue.cpp) · [Python](python/queue.py)

---

### 5. Hash Map / Hash Set

Stores key-value pairs (map) or unique keys (set) in a hash table. Average O(1) for insert, delete, and lookup. Backed by an array of buckets; collisions resolved via chaining or open addressing. A **hash set** is a map where only keys matter (`std::unordered_set` / Python `set`).

**When to use:** frequency counting, two-sum style lookups, deduplication, caching, grouping.  
**Watch out for:** worst-case O(n) on hash collisions; unordered iteration order; high load factor degrades performance.

Examples: [C++](cpp/hash_map.cpp) · [Python](python/hash_map.py)

---

### 6. BST / AVL / Red-Black Tree

#### Plain BST
Each node satisfies: left subtree values < node < right subtree values. Simple but degenerates to O(n) on sorted input.

#### AVL Tree
Height-balanced BST: the height difference between left and right subtrees of any node is at most 1. Balance is restored via **single/double rotations** after each insert or delete. Guarantees O(log n) for all operations. More rigidly balanced than Red-Black → faster lookups, more rotations on writes.

| | Lookup | Insert | Delete | Balance condition |
|---|---|---|---|---|
| **AVL** | O(log n) | O(log n) | O(log n) | \|height(L) − height(R)\| ≤ 1 |
| **Red-Black** | O(log n) | O(log n) | O(log n) | No path is 2× longer than another |

#### Red-Black Tree
A BST where every node is coloured red or black. Five invariants (root is black, no two adjacent reds, equal black-height on all root-to-leaf paths, …) keep the tree approximately balanced. Fewer rotations than AVL on writes. Used by `std::map`/`std::set` in most STL implementations and Java's `TreeMap`.

**When to use:** sorted collection with fast insert/delete/search; successor/predecessor; order-statistics. Prefer AVL when reads dominate; Red-Black when writes are frequent.  
**Watch out for:** plain BST with sorted input degrades to O(n); always use a self-balancing variant in production.

Examples: [C++ (BST + AVL)](cpp/bst.cpp) · [Python (BST + AVL)](python/bst.py)

---

### 7. Heap

A complete binary tree satisfying the heap property (min-heap: parent ≤ children). Efficiently exposes the minimum (or maximum) element. Implemented as an array.

**When to use:** priority queues, Dijkstra's algorithm, heap sort, k-th element problems.  
**Watch out for:** no O(1) arbitrary lookup; only the root is O(1) accessible.

Examples: [C++](cpp/heap.cpp) · [Python](python/heap.py)

---

### 8. Graph

A set of vertices (V) connected by edges (E). Represented as an adjacency list (sparse graphs) or adjacency matrix (dense graphs). Can be directed/undirected and weighted/unweighted.

**When to use:** path finding (BFS/DFS/Dijkstra), connectivity, topological sort, cycle detection.  
**Watch out for:** adjacency matrix is O(V²) space; choose representation based on density.

Examples: [C++](cpp/graph.cpp) · [Python](python/graph.py)

---

### 9. Trie

A tree where each node represents a character prefix. All descendants of a node share its prefix. Lookup and insert are O(m) where m is key length — independent of the number of stored keys.

**When to use:** prefix search, autocomplete, word-existence checks, longest common prefix.  
**Watch out for:** high memory usage for large alphabets; a compressed (Patricia) trie helps.

Examples: [C++](cpp/trie.cpp) · [Python](python/trie.py)

---

### 10. Union-Find (Disjoint Set)

Maintains a collection of disjoint sets and supports two operations: **union** (merge two sets) and **find** (determine which set an element belongs to). With **path compression** and **union by rank**, both operations are effectively O(1) — technically O(α(n)) where α is the inverse Ackermann function.

**When to use:** connected components, Kruskal's MST algorithm, cycle detection in undirected graphs, network connectivity problems.  
**Watch out for:** does not support splitting a set; deletion is non-trivial.

Examples: [C++](cpp/union_find.cpp) · [Python](python/union_find.py)

---

### 11. Segment Tree

A binary tree built on top of an array that supports both **range queries** (sum, min, max over [l, r]) and **point updates** in O(log n). Each node stores the aggregate of its subtree. A **Lazy Segment Tree** extends this to support range updates in O(log n) as well.

**When to use:** range sum/min/max queries with frequent updates; problems asking for the "best subarray" meeting a condition.  
**Watch out for:** high constant factor — for static arrays, a prefix sum array suffices with O(1) range queries.

Examples: [C++](cpp/segment_tree.cpp) · [Python](python/segment_tree.py)

---

### 12. Bloom Filter

A space-efficient probabilistic data structure that tests whether an element is **definitely not** in a set or **possibly** in it. Uses k independent hash functions mapping to a bit array. False positives are possible; false negatives are not. Deletion is not supported in the basic version (Counting Bloom Filter adds deletion).

**When to use:** membership testing where false positives are acceptable and memory is constrained — cache pre-filtering, spell checkers, network routers (e.g. detecting malicious URLs), deduplication pipelines.  
**Watch out for:** false positive rate grows with load; choose bit array size and k for the desired error rate.

Examples: [C++](cpp/bloom_filter.cpp) · [Python](python/bloom_filter.py)

---

## References

### Quick Learning (start here)
- [NeetCode — Data Structures for Beginners](https://neetcode.io/courses/dsa-for-beginners/0) — short video lessons with visualisations
- [CS Visualized: Data Structures](https://dev.to/lydiahallie/cs-visualized-data-structures-k5f) — animated explanations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — complexity reference card
- [LeetCode Explore — Data Structures](https://leetcode.com/explore/learn/) — hands-on problems per topic
- [Visualgo](https://visualgo.net/en) — interactive step-by-step algorithm/DS visualiser

### Deeper Dives
- [GeeksForGeeks — DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
- [Programiz — DSA](https://www.programiz.com/dsa) — clean text explanations with diagrams
- [CP-Algorithms](https://cp-algorithms.com/) — competitive-programming-level depth
- **Book:** *Introduction to Algorithms* (CLRS) — the standard academic reference
- **Book:** *The Algorithm Design Manual* (Skiena) — practical and interview-focused
  