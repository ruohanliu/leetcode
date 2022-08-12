class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
            #subsequence #iter #combination #permutation
        """
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        candidate = []
        c = Counter(s)
        for x in c:
            candidate.extend([x]*(c[x]//k))
        n = len(candidate)
        
        todo = set()
        for i in range(n+1):
            for comb in combinations(candidate,i):
                for perm in permutations(comb):
                    todo.add("".join(perm))
        todo = sorted(todo,key = lambda x:(len(x),x), reverse = True)
        for cand in todo:
            if isSubsequence(cand*k,s):
                return cand
           
