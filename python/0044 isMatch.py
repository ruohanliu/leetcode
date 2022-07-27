class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            #dp
        """
        n = len(s)
        m = len(p)

        # dp[i][j] denotes s[:i+1] matches p[:j+1]
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1,m+1):
            if p[i-1] == "*":
                # find the first s index where dp is true
                s_index = 1
                while not dp[s_index-1][i-1] and s_index < n+1:
                    s_index += 1

                dp[s_index-1][i] = dp[s_index-1][i-1]

                while s_index < n+1:
                    dp[s_index][i] = dp[s_index-1][i]
                    s_index += 1

            elif p[i-1] == "?":
                for j in range(1,n+1):
                    dp[j][i] = dp[j-1][i-1]

            else:
                for j in range(i,n+1):
                    dp[j][i] = dp[j-1][i-1] and s[j-1] == p[j-1]
        return dp[n][m]

