import re


class Solution:
    def strangePrinter(self, s: str) -> int:
        """
            #dp #relation
        """
        @cache
        def dp(i,j):
            if i == j:
                return 1
            if i+1 == j:
                return 1 if s[i] == s[j] else 2
            return min(dp(i,k)+dp(k+1,j) for k in range(i,j)) + (-1 if s[i] == s[j] else 0)

        s = "".join(a for a, b in zip(s, '#' + s) if a != b)
        return dp(0,len(s)-1)
                