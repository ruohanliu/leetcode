class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
            #dp #relation #bottomuporder
        """
        cuts = sorted(cuts+[0,n])
        k = len(cuts)
        dp = [[0] * k for _ in range(k)]
        for gap in range(2,k):
            for i in range(k-gap):
                j = i + gap
                dp[i][j] = min(dp[i][mid] + dp[mid][j] for mid in range(i+1,j)) + cuts[j] - cuts[i]

        return dp[0][k-1]

    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dp(i,j):
            if j - i <= 1:
                return 0
            return min(dp(i,mid) + dp(mid,j) for mid in range(i+1,j)) + cuts[j] - cuts[i]

        cuts = sorted(cuts+[0,n])
        k = len(cuts)
        return dp(0,k-1)