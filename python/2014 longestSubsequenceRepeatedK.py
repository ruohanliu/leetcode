class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
            #subsequence #iter #combination #permutation
        """
        def isSubsequence(s,t):
            it = iter(t)
            return all(c in it for c in s)
        
        candidate = []
        c = Counter(s)
        for x in c:
            candidate.extend([x]*(c[x]//k))
        n = len(candidate)
        
        todo = set()
        for i in range(n+1):
            for perm in permutations(candidate,i):
                todo.add("".join(perm))
        
        for cand in sorted(todo,key = lambda x:(len(x),x), reverse = True):
            if isSubsequence(cand*k,s):
                return cand
           
