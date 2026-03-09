// BST / AVL / Red-Black Tree
// - Plain BST  : simple, O(n) worst case on sorted input
// - AVL Tree   : height-balanced via rotations, O(log n) guaranteed
// - Red-Black  : std::map / std::set (STL uses RB tree internally)
#include <algorithm>
#include <iostream>
#include <map>
#include <set>

// ============================================================
// 1. Plain BST
// ============================================================
struct BSTNode {
    int val;
    BSTNode* left = nullptr;
    BSTNode* right = nullptr;
    explicit BSTNode(int v) : val(v) {}
};

BSTNode* bst_insert(BSTNode* root, int val) {
    if (!root) return new BSTNode(val);
    if (val < root->val) root->left  = bst_insert(root->left,  val);
    else if (val > root->val) root->right = bst_insert(root->right, val);
    return root;
}

bool bst_search(BSTNode* root, int val) {
    while (root) {
        if (val == root->val) return true;
        root = (val < root->val) ? root->left : root->right;
    }
    return false;
}

void inorder(BSTNode* root) {
    if (!root) return;
    inorder(root->left);
    std::cout << root->val << " ";
    inorder(root->right);
}

void destroy(BSTNode* root) {
    if (!root) return;
    destroy(root->left);
    destroy(root->right);
    delete root;
}

// ============================================================
// 2. AVL Tree
// ============================================================
struct AVLNode {
    int val, height;
    AVLNode* left = nullptr;
    AVLNode* right = nullptr;
    explicit AVLNode(int v) : val(v), height(1) {}
};

int height(AVLNode* n) { return n ? n->height : 0; }
int balanceFactor(AVLNode* n) { return n ? height(n->left) - height(n->right) : 0; }

void updateHeight(AVLNode* n) {
    if (n) n->height = 1 + std::max(height(n->left), height(n->right));
}

//      y                x
//     / \              / \
//    x   C   --->    A    y
//   / \                  / \
//  A   B                B   C
AVLNode* rotateRight(AVLNode* y) {
    AVLNode* x = y->left;
    AVLNode* B = x->right;
    x->right = y;
    y->left  = B;
    updateHeight(y);
    updateHeight(x);
    return x;   // new root
}

AVLNode* rotateLeft(AVLNode* x) {
    AVLNode* y = x->right;
    AVLNode* B = y->left;
    y->left  = x;
    x->right = B;
    updateHeight(x);
    updateHeight(y);
    return y;
}

AVLNode* avl_insert(AVLNode* node, int val) {
    if (!node) return new AVLNode(val);
    if (val < node->val) node->left  = avl_insert(node->left,  val);
    else if (val > node->val) node->right = avl_insert(node->right, val);
    else return node;  // duplicate

    updateHeight(node);
    int bf = balanceFactor(node);

    // Left-Left
    if (bf > 1 && val < node->left->val)  return rotateRight(node);
    // Right-Right
    if (bf < -1 && val > node->right->val) return rotateLeft(node);
    // Left-Right
    if (bf > 1 && val > node->left->val) {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }
    // Right-Left
    if (bf < -1 && val < node->right->val) {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }
    return node;
}

void avl_inorder(AVLNode* node) {
    if (!node) return;
    avl_inorder(node->left);
    std::cout << node->val << "(h" << node->height << ") ";
    avl_inorder(node->right);
}

void avl_destroy(AVLNode* node) {
    if (!node) return;
    avl_destroy(node->left);
    avl_destroy(node->right);
    delete node;
}

// ============================================================
// 3. Red-Black Tree — STL std::map / std::set
//    The C++ standard mandates O(log n) for map operations;
//    most implementations (GCC libstdc++, MSVC, Clang libc++)
//    use a Red-Black tree internally.
// ============================================================

int main() {
    // --- Plain BST ---
    BSTNode* bst = nullptr;
    for (int v : {5, 3, 7, 1, 4, 6, 8}) bst = bst_insert(bst, v);
    std::cout << "BST in-order:  ";
    inorder(bst);
    std::cout << "\n";
    std::cout << "BST search 4:  " << std::boolalpha << bst_search(bst, 4) << "\n";
    std::cout << "BST search 9:  " << bst_search(bst, 9) << "\n";
    destroy(bst);

    // --- AVL Tree ---
    // Inserting in sorted order degrades BST to O(n); AVL stays O(log n)
    AVLNode* avl = nullptr;
    for (int v : {1, 2, 3, 4, 5, 6, 7}) avl = avl_insert(avl, v);
    std::cout << "\nAVL in-order (with heights): ";
    avl_inorder(avl);
    std::cout << "\n";
    std::cout << "AVL root: " << avl->val << ", root height: " << avl->height << "\n";
    avl_destroy(avl);

    // --- Red-Black Tree via std::map ---
    std::map<int, std::string> rb;
    for (auto [k, v] : std::initializer_list<std::pair<int,const char*>>{
            {5,"five"},{3,"three"},{7,"seven"},{1,"one"},{4,"four"}})
        rb[k] = v;

    std::cout << "\nstd::map (RB tree, sorted keys):\n";
    for (const auto& [k, v] : rb) std::cout << "  " << k << " -> " << v << "\n";

    // Successor of 3
    auto it = rb.upper_bound(3);
    std::cout << "Successor of 3: " << it->first << "\n";

    // --- std::set: Red-Black tree, unique sorted values ---
    std::set<int> s = {5, 3, 7, 1, 4, 6, 8};
    s.insert(2);
    s.erase(7);
    std::cout << "\nstd::set: ";
    for (int x : s) std::cout << x << " ";
    std::cout << "\n";

    return 0;
}
