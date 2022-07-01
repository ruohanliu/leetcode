class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        """
            #bitwise
        """
        seen = set()
        ans = 0
        for word in startWords:
            bitmask = 0
            for c in word:
                bitmask ^= 1 << ord(c)-97
            seen.add(bitmask)
            
        for word in targetWords:
            bitmask = 0
            for c in word:
                bitmask ^= 1<<ord(c)-97
            for c in word:
                if bitmask ^ 1<<ord(c)-97 in seen:
                    ans += 1
                    break
        return ans

    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        """
            #trie
        """
        trie = Trie()
        ans = 0
        for word in startWords:
            trie.insert(sorted(word))
        for word in targetWords:
            word = sorted(word)
            ans += any(trie.search(word,i) for i in range(len(word))) 
        return ans

class TrieNode:
    def __init__(self):
        self.ends = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.ends = True

    def search(self, word: str,skipIndex) -> bool:
        node = self.root
        for i,c in enumerate(word):
            if i == skipIndex: continue
            if c not in node.children:
                return False
            node = node.children[c]
        return node.ends
