// Linked List — using std::list (doubly-linked) and std::forward_list (singly-linked)
#include <forward_list>
#include <iostream>
#include <list>

int main() {
    // --- Doubly-linked list ---
    std::list<int> dl = {10, 20, 30};
    dl.push_front(5);    // O(1)
    dl.push_back(40);    // O(1)

    // Remove all occurrences of a value — O(n)
    dl.push_back(20);
    dl.remove(20);

    std::cout << "Doubly-linked list: ";
    for (int x : dl) std::cout << x << " ";
    std::cout << "\n";

    // Iterator-based insertion (O(1) given the iterator)
    auto it = dl.begin();
    std::advance(it, 2);
    dl.insert(it, 99);

    std::cout << "After insert at pos 2: ";
    for (int x : dl) std::cout << x << " ";
    std::cout << "\n";

    // --- Singly-linked list ---
    std::forward_list<int> sl = {1, 2, 3};
    sl.push_front(0);           // O(1)
    sl.insert_after(sl.begin(), 10); // O(1)

    std::cout << "Singly-linked list: ";
    for (int x : sl) std::cout << x << " ";
    std::cout << "\n";

    return 0;
}
