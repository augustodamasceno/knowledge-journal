// Trie (Prefix Tree) — stores strings for O(m) insert/search/prefix-check
#include <array>
#include <iostream>
#include <string>

struct TrieNode {
    std::array<TrieNode*, 26> children{};
    bool isEnd = false;

    ~TrieNode() {
        for (TrieNode* child : children) delete child;
    }
};

class Trie {
public:
    Trie() : root(new TrieNode()) {}
    ~Trie() { delete root; }

    // O(m) — m = word length
    void insert(const std::string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    // O(m) — exact word search
    bool search(const std::string& word) const {
        TrieNode* node = find(word);
        return node && node->isEnd;
    }

    // O(m) — check if any word has this prefix
    bool startsWith(const std::string& prefix) const {
        return find(prefix) != nullptr;
    }

private:
    TrieNode* root;

    TrieNode* find(const std::string& s) const {
        TrieNode* node = root;
        for (char c : s) {
            int idx = c - 'a';
            if (!node->children[idx]) return nullptr;
            node = node->children[idx];
        }
        return node;
    }
};

int main() {
    Trie trie;
    for (const std::string& w : {"apple", "app", "application", "apply", "banana"})
        trie.insert(w);

    std::cout << std::boolalpha;
    std::cout << "search(\"app\"):         " << trie.search("app")         << "\n";
    std::cout << "search(\"apple\"):       " << trie.search("apple")       << "\n";
    std::cout << "search(\"ap\"):          " << trie.search("ap")          << "\n";
    std::cout << "startsWith(\"app\"):     " << trie.startsWith("app")     << "\n";
    std::cout << "startsWith(\"ban\"):     " << trie.startsWith("ban")     << "\n";
    std::cout << "startsWith(\"cat\"):     " << trie.startsWith("cat")     << "\n";

    return 0;
}
