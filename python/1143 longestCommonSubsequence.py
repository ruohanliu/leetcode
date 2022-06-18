class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * n for _ in range(m)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]


    def longestCommonSubsequence_space_optimizaed(self, text1: str, text2: str) -> int:
        """
            #dp #spaceoptimize #important
        """
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # text1 < text2
        m = len(text1)
        n = len(text2)
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

        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return lcs(i+1,j+1) + 1
            else:
                return max(lcs(i, j+1), lcs(i+1, j))
        return lcs(0,0)