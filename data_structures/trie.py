# Trie


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def print_trie(self):
        current = self.root
        self.print_helper(current)

    def print_helper(self, current):
        for char in current.children:
            print(char)
            self.print_helper(current.children[char])


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.insert('app')
    trie.insert('apricot')
    trie.insert('apocalypse')
    trie.insert('banana')
    trie.insert('bananas')
    trie.insert('bananarama')
    trie.insert('bananaramas')
    trie.insert('bananaramarama')
    trie.insert('bananaramaramas')
    trie.insert('bananaramaramarama')
    trie.insert('bananaramaramaramas')
    trie.insert('bananaramaramaramarama')
    trie.insert('bananaramaramaramaramas')
    trie.insert('bananaramaramaramaramarama')
    trie.insert('bananaramaramaramaramaramas')
    trie.insert('bananaramaramaramaramaramarama')
    trie.insert('bananaramaramaramaramaramaramas')
    trie.insert('bananaramaramaramaramaramaramarama')
    trie.insert('bananaramaramaramaramaramaramaramas')
    trie.insert('bananaramaramaramaramaramaramaramarama')
    trie.insert('bananaramaramaramaramaramaramaramaramas')
    trie.insert('bananaramaramaramaramaramaramaramaramarama')
    trie.insert('bananaramaramaramaramaramaramaramaramaramas')
    trie.insert('banana split')
    trie.insert('banana split with chocolate')
    trie.insert('banana split with chocolate and sprinkles')

    print(trie.search('apple'))
    print(trie.search('app'))
