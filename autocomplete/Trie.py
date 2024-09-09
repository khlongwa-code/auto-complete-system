class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_words(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):
        node = self.search_prefix(prefix)
        if not node:
            return []

        suggestions = []
        self._find_words(node, prefix, suggestions)
        return suggestions

    def _find_words(self, node, prefix, suggestions):
        
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, suggestions)
    
    def populate_trie(self):
        words = ["cat", "car", "cart", "carbon", "dog", "dove", "door"]

        for word in words:
            self.insert_words(word)
    
    def run_autocomplete(self):
        self.populate_trie()

        prefix = input("Enter prefix to autocomplete: ")
        suggestions = self.autocomplete(prefix)
        
        if suggestions:
            print(f"Suggestions for '{prefix}': {suggestions}")
        else:
            print(f"No suggestions found for '{prefix}'")

if __name__ == "__main__":
    trie = Trie()
    trie.run_autocomplete()