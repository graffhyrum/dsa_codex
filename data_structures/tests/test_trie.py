import unittest

from data_structures.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):  # Use setUp method for initialization
        self.test_strings = [
            'apple',
            'app',
            'apricot',
            'apocalypse',
            'banana',
            'bananas',
            'bananarama',
            'bananaramas',
            'bananaramarama',
            'bananaramaramas',
            'bananaramaramarama',
            'bananaramaramaramas'
        ]
        self.trie = Trie()
        for string in self.test_strings:
            self.trie.insert(string)

    def test_insert(self):
        inserted_string = 'calypso'
        x = self.trie.search(inserted_string)
        self.assertFalse(x)
        self.trie.insert(inserted_string)
        x = self.trie.search(inserted_string)
        self.assertTrue(x)

    def test_search(self):
        for string in self.test_strings:
            self.assertTrue(self.trie.search(string))
        self.assertFalse(self.trie.search('calypso'))

    def test_starts_with(self):
        first_letters = set([string[0] for string in self.test_strings])
        for letter in first_letters:
            self.assertTrue(self.trie.starts_with(letter))
        self.assertFalse(self.trie.starts_with('c'))
