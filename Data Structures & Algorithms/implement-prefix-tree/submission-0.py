class TrieNode: # a single node in the tree. since we are constructing a tree data structure, we need to have this as the most basic level node
    def __init__(self):
        self.children = {} # hashable set o(1) lookup
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None: # to insert, we need to get each char
                                         # iterate down the tree if that char exists, and add a new letter if that char doesnt exist at that level of the word, ending 
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() # if this happens, every future insert will activate this if statement
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        