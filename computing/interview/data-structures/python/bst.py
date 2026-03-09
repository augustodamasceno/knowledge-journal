# BST / AVL / Red-Black Tree
# - Plain BST : simple recursive implementation
# - AVL Tree  : height-balanced with single/double rotations
# - Red-Black : sortedcontainers.SortedList (C-accelerated, O(log n))


# ============================================================
# 1. Plain BST
# ============================================================
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val) -> bool:
        node = self.root
        while node:
            if val == node.val:
                return True
            node = node.left if val < node.val else node.right
        return False

    def inorder(self) -> list:
        result = []
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            result.append(node.val)
            _walk(node.right)
        _walk(self.root)
        return result


# ============================================================
# 2. AVL Tree  (height-balanced, O(log n) guaranteed)
# ============================================================
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1


def _height(node):
    return node.height if node else 0

def _update_height(node):
    node.height = 1 + max(_height(node.left), _height(node.right))

def _balance_factor(node):
    return _height(node.left) - _height(node.right)

def _rotate_right(y):
    #      y                x
    #     / \              / \
    #    x   C   --->    A    y
    #   / \                  / \
    #  A   B                B   C
    x = y.left
    y.left = x.right
    x.right = y
    _update_height(y)
    _update_height(x)
    return x

def _rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    _update_height(x)
    _update_height(y)
    return y

def avl_insert(node, val):
    if not node:
        return AVLNode(val)
    if val < node.val:
        node.left = avl_insert(node.left, val)
    elif val > node.val:
        node.right = avl_insert(node.right, val)
    else:
        return node  # duplicate

    _update_height(node)
    bf = _balance_factor(node)

    # Left-Left
    if bf > 1 and val < node.left.val:
        return _rotate_right(node)
    # Right-Right
    if bf < -1 and val > node.right.val:
        return _rotate_left(node)
    # Left-Right
    if bf > 1 and val > node.left.val:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)
    # Right-Left
    if bf < -1 and val < node.right.val:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node

def avl_inorder(node, result=None):
    if result is None:
        result = []
    if not node:
        return result
    avl_inorder(node.left, result)
    result.append((node.val, node.height))
    avl_inorder(node.right, result)
    return result


# ============================================================
# Demos
# ============================================================

# --- Plain BST ---
bst = BST()
for v in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(v)
print("BST in-order:", bst.inorder())
print("BST search 4:", bst.search(4))
print("BST search 9:", bst.search(9))

# Worst case: sorted input makes plain BST degenerate (height = n)
bst_sorted = BST()
for v in range(1, 8):
    bst_sorted.insert(v)
print("BST sorted insert in-order:", bst_sorted.inorder())

# --- AVL Tree: sorted input stays balanced ---
avl_root = None
for v in range(1, 8):
    avl_root = avl_insert(avl_root, v)
print("\nAVL in-order (val, height):", avl_inorder(avl_root))
print("AVL root:", avl_root.val, "height:", avl_root.height)

# --- Red-Black / balanced BST via sortedcontainers ---
try:
    from sortedcontainers import SortedList, SortedDict
    sl = SortedList([5, 3, 7, 1, 4, 6, 8])
    sl.add(2)
    sl.discard(7)
    print("\nSortedList:", list(sl))
    print("Index of 4:", sl.index(4))
    print("Values >= 4:", list(sl.irange(4)))

    sd = SortedDict({5: "five", 3: "three", 7: "seven"})
    print("\nSortedDict:", list(sd.items()))
    print("Successor of 3:", next(iter(sd.irange(4))))
except ImportError:
    print("\nsortedcontainers not installed — run: pip install sortedcontainers")

