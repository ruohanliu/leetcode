class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
            #trie #binarysearch
        """
        products.sort()
        ans, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            ans.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return ans

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root
        
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] 
            if len(node.words) < 3:
                node.words.append(word)
        
    def search(self, c):
        if self.node and c in self.node.children: 
            self.node = self.node.children[c] 
            return self.node.words
        else: 
            self.node = None    
            return []
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.add(word)
        return [trie.search(c) for c in searchWord]