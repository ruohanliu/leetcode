class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            #re #backtrack #important #edge

            implement . and *
        """
        @cache
        def backtrack(i,j):
            if i >= len(s) and j == len(p):
                return True
            elif j == len(p):
                return False
            if j < len(p)-1 and p[j+1] == "*":
                if p[j] == ".":
                    return any(backtrack(k,j+2) for k in reversed(range(i,len(s)+1)))
                else:
                    return any(backtrack(k,j+2) and s[i:k] == p[j]*(k-i) for k in range(i,len(s)+1))
            elif p[j] == ".":
                return i < len(s) and backtrack(i+1,j+1)
            else:
                if i >= len(s) or s[i] != p[j]:
                    return False
                return backtrack(i+1,j+1)

        return backtrack(0,0)
    