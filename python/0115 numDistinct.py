class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            #dp
        """
        @cache
        def dp(i,j):
            if n - i < m - j:
                return 0
            if j == m:
                return 1
            if s[i] == t[j]:
                return dp(i+1,j+1) + dp(i+1,j)
            else:
                return dp(i+1,j)
        n = len(s)
        m = len(t)
        return dp(0,0)