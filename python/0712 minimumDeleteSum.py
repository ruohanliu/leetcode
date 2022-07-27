class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
            #dp
            related: 1143 longest common subsequence
        """
        m = len(s1)
        n = len(s2)

        # dp stores the difference sum
        dp = [[0]*(n+1) for _ in range(m+1)]

        # initialize corner case
        for i in reversed(range(m)):
            dp[i][n] = dp[i+1][n] + ord(s1[i])
        for j in reversed(range(n)):
            dp[m][j] = dp[m][j+1] + ord(s2[j])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        return dp[0][0]

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
            #dp #spaceoptimize #important
        """
        if len(s2) < len(s1):
            s1, s2 = s2, s1

        m = len(s1)
        n = len(s2)

        prev = [0] * (m+1)
        curr = [0] * (m+1)

        for i in reversed(range(m)):
            prev[i] = prev[i+1] + ord(s1[i])

        for i in reversed(range(n)):
            curr[m] = ord(s2[i])+prev[m]
            for j in reversed(range(m)):
                if s1[j] == s2[i]:
                    curr[j] = prev[j+1]
                else:
                    curr[j] = min(curr[j+1] + ord(s1[j]), prev[j] + ord(s2[i]))
            prev, curr = curr, prev
        return prev[0]
