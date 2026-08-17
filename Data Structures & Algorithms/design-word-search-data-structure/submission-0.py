class CharNode:
    def __init__(self):
        self.children = {} # char:charNode
        self.word = False

class WordDictionary:
    # must be able to add words in 0(n) time
    # must be able to search words in 0(n) time
    def __init__(self):
        self.root = CharNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # means we have to add this letter
                cur.children[c] = CharNode()
            cur = cur.children[c] # iterate to next level
        cur.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)): # from the . level to the bottom
                c = word[i]
                if c == ".": # check all possibilities with this as the root
                    for child in cur.children.values():
                        if dfs(i+1, child): return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)
                        
            