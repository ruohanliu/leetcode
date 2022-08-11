 class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
            #dp #math #important #probability
        """
        if k == 0 or n >= k + maxPts:
            return 1
        dp = [0.0] * (n+1)
        dp[0] = 1.0
        total = 1.0

        for i in range(1,n+1):
            dp[i] = total / maxPts
            if i < k:
                total += dp[i]
            if i >= maxPts:
                total -= dp[i-maxPts]
        return sum(dp[k:])