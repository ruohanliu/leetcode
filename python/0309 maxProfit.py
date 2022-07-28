class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            #dp #important #statemachine #optimization #stock
        """
        n = len(prices)
        if n < 2:
            return 0
        buy = [0] * (n+2)
        sell = [0] * (n+2)
        buy[1] = -prices[0]

        for i in range(2,n+2):
            buy[i] = max(sell[i-2]-prices[i-2],buy[i-1])
            sell[i] = max(buy[i]+prices[i-2],sell[i-1])
        return sell[-1]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]

        for i in reversed(range(n)):
            for holding in range(2):
                if holding:
                    dp[i][holding] = max(prices[i]+dp[i+2][holding ^ 1],dp[i+1][holding])
                else:
                    dp[i][holding] = max(-prices[i]+dp[i+1][holding ^ 1],dp[i+1][holding])
        return dp[0][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
            #stock #dp
        """
        @cache
        def dp(i,holding):
            nonlocal n
            if i >= n:
                return 0
            
            if holding:
                return max(prices[i] + dp(i+2,False),dp(i+1,True))
            else:
                return max(-prices[i] + dp(i+1,True),dp(i+1,False))

        n = len(prices)
        return dp(0,False)