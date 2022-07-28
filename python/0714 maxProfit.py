class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
            #dp #optimization 

            related 0309
            https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        """
        n = len(prices)
        if n < 2:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1,n):
            buy = max(sell-prices[i],buy)
            sell = max(buy+prices[i]-fee,sell)
        return sell

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0]*2 for _ in range(n+1)]
        for i in reversed(range(n)):
            for holding in range(2):
                if holding:
                    dp[i][holding] = max(prices[i] + dp[i+1][holding^1]-fee,dp[i+1][holding])
                else:
                    dp[i][holding] = max(-prices[i] + dp[i+1][holding^1],dp[i+1][holding])
        return dp[0][0]
