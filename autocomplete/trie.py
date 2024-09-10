class TrieNode:
    """
    Represents a single node in the Trie structure. Each node stores its children
    and a boolean flag to indicate if it is the end of a word.
    """

    def __init__(self):

        """
        Initialize the TrieNode with an empty dictionary to store children nodes
        and a flag to indicate whether this node marks the end of a valid word.
        """

        self.children = {}
        self.is_end_of_word = False

class Trie:

    """
    Trie data structure for efficient insertion and retrieval of words based on their prefixes.
    """

    def __init__(self):

        """
        Initialize the Trie with a root node. The root node does not contain any character
        but serves as the starting point for all insertions and searches.
        """

        self.root = TrieNode()

    def insert_words(self, word):

        """
        Insert a word into the Trie. Each character of the word is stored as a node,
        and the final character is marked as the end of a word.
        
        Args:
            word (str): The word to be inserted into the Trie.
        """
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):

        """
        Search for a prefix in the Trie and return the node at the end of the prefix.
        
        Args:
            prefix (str): The prefix to search for in the Trie.
        
        Returns:
            TrieNode or None: The node where the prefix ends, or None if the prefix is not found.
        """
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):

        """
        Given a prefix, find and return all words in the Trie that start with that prefix.
        
        Args:
            prefix (str): The prefix to autocomplete.

        Returns:
            list: A list of words that start with the given prefix.
        """
        
        node = self.search_prefix(prefix)
        if not node:
            return []

        suggestions = []
        self._find_words(node, prefix, suggestions)
        return suggestions

    def _find_words(self, node, prefix, suggestions):

        """
        A helper function to recursively find all the words that start with the given prefix.

        Args:
            node (TrieNode): The current node in the Trie traversal.
            prefix (str): The current word being formed.
            suggestions (list): The list to store the found words.
        """
        
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, suggestions)
    
    def populate_trie(self):

        """
        Populate the Trie with a predefined set of words for testing and demonstration purposes.
        """

        words = ["cat", "car", "cart", "carbon", "dog", "dove", "door"]

        for word in words:
            self.insert_words(word)
    
    def run_autocomplete(self):

        """
        Run a simple command-line-based autocomplete feature. Prompts the user to enter a prefix
        and returns suggestions based on that prefix.
        """
        
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