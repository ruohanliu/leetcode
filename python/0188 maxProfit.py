class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
            #stock #dp
        """
        @cache
        def dp(i,k,holding):
            nonlocal n
            if n == i or k == 0:
                return 0
            
            if holding:
                return max(prices[i] + dp(i+1,k-1,False),dp(i+1,k,True))
            else:
                return max(-prices[i] + dp(i+1,k,True),dp(i+1,k,False))

        n = len(prices)
        return dp(0,k,False)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n+1)]

        for i in reversed(range(n)):
            for k in range(1,k+1):
                for holding in range(2):
                    if holding:
                        dp[i][k][holding] = max(prices[i]+dp[i+1][k-1][holding ^ 1],dp[i+1][k][holding])
                    else:
                        dp[i][k][holding] = max(-prices[i]+dp[i+1][k][holding ^ 1],dp[i+1][k][holding])
        return dp[0][k][0]
