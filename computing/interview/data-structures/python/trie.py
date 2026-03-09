# Trie (Prefix Tree) — O(m) insert/search/prefix-check (m = key length)


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):          # O(m)
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:  # O(m) — exact match
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:  # O(m)
        return self._find(prefix) is not None

    def autocomplete(self, prefix: str) -> list[str]:
        """Return all words starting with prefix."""
        node = self._find(prefix)
        if not node:
            return []
        results: list[str] = []
        self._collect(node, prefix, results)
        return results

    def _find(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _collect(self, node: TrieNode, current: str, results: list[str]):
        if node.is_end:
            results.append(current)
        for ch, child in node.children.items():
            self._collect(child, current + ch, results)


# --- Demo ---
trie = Trie()
for w in ["apple", "app", "application", "apply", "banana"]:
    trie.insert(w)

print("search('app'):", trie.search("app"))           # True
print("search('apple'):", trie.search("apple"))       # True
print("search('ap'):", trie.search("ap"))             # False
print("starts_with('app'):", trie.starts_with("app")) # True
print("starts_with('cat'):", trie.starts_with("cat")) # False
print("autocomplete('app'):", sorted(trie.autocomplete("app")))
print("autocomplete('ban'):", trie.autocomplete("ban"))
