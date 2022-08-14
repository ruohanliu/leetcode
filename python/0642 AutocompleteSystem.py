class TrieNode:
    def __init__(self):
        self.sentences = set()
        self.child = defaultdict(TrieNode)
class AutocompleteSystem:
    """
        #trie

        alternatively store count in each trie node to reduce space usage at cost of dfs searching time
        def dfs(self, root):
            ret = []
            if root:
                if root.isEnd:
                    ret.append((root.rank, root.data))
                for child in root.children:
                    ret.extend(self.dfs(root.children[child]))
            return ret
            
        def search(self, sentence):
            p = self.root
            for c in sentence:
                if c not in p.children:
                    return []
                p = p.children[c]
            return self.dfs(p)
    """
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        self.count = defaultdict(int)
        for sentence,time in zip(sentences,times):
            self.count[sentence] = time
            self._add_sentence(sentence)
        
    def _add_sentence(self,sentence):
        node = self.root
        for c in sentence:
            node = node.child[c]
            node.sentences.add(sentence)

    def _find(self,sentence):
        node = self.root
        for c in sentence:
            node = node.child.get(c)
            if not node:
                return []
        return sorted(node.sentences, key = lambda x:(-self.count[x],x))[:3]

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.keyword += c
            return self._find(self.keyword)
        self._add_sentence(self.keyword)
        self.count[self.keyword] += 1
        self.keyword = ""
        return []