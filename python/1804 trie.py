class TrieNode:
    def __init__(self):
        self.ends = 0
        self.children = {}

class Trie:
    """
        #trie
    """
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.ends += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.ends

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        ans = 0
        queue = [node]
        while queue:
            node = queue.pop()
            ans += node.ends
            for c in node.children:
                queue.append(node.children[c])
        return ans

    def erase(self, word: str) -> None:
        node = self.root
        parent = None
        for c in word:
            if c not in node.children:
                return
            parent = node
            node = node.children[c]
        node.ends -= 1
        if not node.children and not node.ends:
            del parent.children[c]
