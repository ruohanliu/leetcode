class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
        
    # print lcs
    def lcs(s,t):
        n = len(s)
        m = len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        ans = []
        i = n
        j = m
        while i and j:
            if s[i-1] == t[j-1]:
                ans += s[i-1],
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return ans[::-1]

    def longestCommonSubsequence_space_optimizaed(self, text1: str, text2: str) -> int:
        """
            #dp #spaceoptimize #important #lcs
            related 1312
        """
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # text1 < text2
        m = len(text1)
        n = len(text2)

        # initialization. base case: there is  0 common char.  for other problems, the initial value could be others.
        prev = [0] * (m+1)
        curr = [0] * (m+1)
        
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if text1[j] == text2[i]:
                    curr[j] = 1+prev[j+1]
                else:
                    curr[j] = max(prev[j],curr[j+1])
            curr,prev = prev,curr
        return prev[0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            #recursion #memoization #important

            functools cache
        """
        from functools import cache

        @cache
        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return lcs(i+1,j+1) + 1
            else:
                return max(lcs(i, j+1), lcs(i+1, j))
        return lcs(0,0)