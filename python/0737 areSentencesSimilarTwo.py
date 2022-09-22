class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        """
            #unionfind #google
        """
        if len(sentence1) != len(sentence2):
            return False

        def find(a):
            if a not in uf:
                uf[a] = a
            _a = a
            while a != uf[a]:
                a = uf[a]
            while _a != a:
                _a,uf[_a] = uf[_a],a
            return a
        
        def union(a, b):
            a = find(a)        
            b = find(b)
            if a == b:
                return False
            if size[a] > size[b]:
                size[a] += size[b]
                uf[b] = a
            else:
                size[b] += size[a]
                uf[a] = b
            return True
                
        uf = {}
        size = defaultdict(lambda:1)
        for a, b in similarPairs:
            union(a, b)
            
        return all(find(a) == find(b) for a, b in zip(sentence1, sentence2))