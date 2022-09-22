class StreamChecker:
    """
        #trie
        initialization: O(WL)

        query: O(L)
    """
    def __init__(self, words: List[str]):
        self.trie = {}
        maxLen = 0
        for word in words:
            node = self.trie
            maxLen = max(maxLen,len(word))
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"] = True
        self.queue = deque([],maxLen)

    def query(self, letter: str) -> bool:
        self.queue.append(letter)
        node = self.trie
        for i in range(len(self.queue)):
            c = self.queue[~i]
            if c not in node:
                return False
            node = node[c]
            if "$" in node:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)