class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
            #dp #palindrome #important
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for k in range(n):
            for l in range(n-k):
                r = l+k
                if l == r:
                    dp[l][r] = 1
                elif l + 1 == r and s[l] == s[r]:
                    dp[l][r] = 2
                elif s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])
        return dp[0][-1]