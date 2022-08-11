class Solution:
    def minInsertions(self, s: str) -> int:
        """
            #palindrome #dp #lcs
            related 1143
            longest palindrome subsequence = longest common subsequence between s and its reverse
        """
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[~j]:
                    dp[i+1][j+1] = 1+dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return n - dp[n][n]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        prev = [0] * (n+1)
        curr = prev[:]
        for i in range(n):
            for j in range(n):
                if s[i] == s[~j]:
                    curr[j+1] = 1+prev[j]
                else:
                    curr[j+1] = max(prev[j+1],curr[j])
            prev,curr = curr,prev
        return n - prev[n]
