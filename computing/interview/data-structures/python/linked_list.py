# Linked List — manual singly-linked list + collections.deque (doubly-linked, O(1) ends)
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val):          # O(1)
        node = Node(val)
        node.next = self.head
        self.head = node

    def append(self, val):           # O(n)
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, val):           # O(n)
        dummy = Node(0)
        dummy.next = self.head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        self.head = dummy.next

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


# --- Manual singly-linked list ---
sll = SinglyLinkedList()
for v in [1, 2, 3, 4]:
    sll.append(v)
sll.prepend(0)
sll.delete(3)
print("Singly-linked list:", sll.to_list())

# --- collections.deque: O(1) at both ends (doubly-linked under the hood) ---
dq = deque([10, 20, 30])
dq.appendleft(5)    # O(1)
dq.append(40)       # O(1)
dq.popleft()        # O(1)
dq.pop()            # O(1)

print("Deque:", list(dq))
print("Access middle (index 1):", dq[1])   # O(n) — deque is not O(1) random access
