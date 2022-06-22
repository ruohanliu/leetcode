from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            #dp #knapsack

            0-1 knapsack problem. DP: O(nW) time and O(W) space

        """
        # dp[i] denotes the least number of coins for a given amount
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for m in range(coin,amount+1):
                dp[m] = min(dp[m],dp[m-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
