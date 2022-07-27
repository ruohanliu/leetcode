class WordDictionary:
    """
        #trie
    """

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = True

    def search(self, word: str) -> bool:
        def __search(node,word):
            for i,c in enumerate(word):
                if c in node:
                    node = node[c]
                else:
                    if c == ".":
                        for x in node:
                            if x != "$" and __search(node[x],word[i+1:]):
                                return True
                    return False
            return "$" in node
        return __search(self.trie,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)