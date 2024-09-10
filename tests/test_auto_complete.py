import unittest
from tests.test_base import captured_io
from io import StringIO
from trie import Trie

class TestAutoComplete(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        words = ["cat", "car", "cart", "carbon", "dog", "dove", "door"]
        for word in words:
            self.trie.insert_words(word)

    def test_prefix_not_found(self):
        node = self.trie.search_prefix("ca")
        self.assertIsNotNone(node)

    def test_prefix_found(self):
        node = self.trie.search_prefix("z")
        self.assertIsNone(node)

    def test_full_word_found(self):
        node = self.trie.search_prefix("car")
        self.assertIsNotNone(node)
    
    def test_full_word_not_found(self):
        node = self.trie.search_prefix("zebra")
        self.assertIsNone(node)

    def test_auto_complete_valid_prefix(self):
        suggestions = self.trie.autocomplete("do")
        self.assertTrue(len(suggestions) > 0)
    
    def test_auto_complete_invalid_prefix(self):
        suggestions = self.trie.autocomplete("ju")
        self.assertTrue(len(suggestions) == 0)
    
    def test_insert_single_words(self):
        self.trie.insert_words("cart")
        node = self.trie.root

        self.assertIn("c", node.children)
        node = node.children['c']
        self.assertIn("a", node.children)
        node = node.children['a']
        self.assertIn("r", node.children)
        node = node.children['r']
        self.assertIn("t", node.children)
        node = node.children['t']
    
    def test_insert_multiple_words(self):
        self.trie.insert_words("cart")
        self.trie.insert_words("dot")
        
        node = self.trie.root

        self.assertIn("c", node.children)
        node = node.children['c']
        self.assertIn("a", node.children)
        node = node.children['a']
        self.assertIn("r", node.children)
        node = node.children['r']
        self.assertIn("t", node.children)
        node = node.children['t']

        node = self.trie.root

        self.assertIn("d", node.children)
        node = node.children['d']
        self.assertIn("o", node.children)
        node = node.children['o']
        self.assertIn("t", node.children)
        node = node.children['t']
    
    def test_run_complete_invalid_prefix(self):
        with captured_io(StringIO('a\n')) as (out, err):
            self.trie.run_autocomplete()

        output = out.getvalue().strip()
        self.assertEqual("Enter prefix to autocomplete: No suggestions found for 'a'", output)

    def test_run_complete_valid_prefix(self):
        with captured_io(StringIO('d\n')) as (out, err):
            self.trie.run_autocomplete()

        output = out.getvalue().strip()
        self.assertEqual("Enter prefix to autocomplete: Suggestions for 'd': ['dog', 'dove', 'door']", output)

if __name__ == '__main__':
    unittest.main()
