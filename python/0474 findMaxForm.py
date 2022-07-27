from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
            #dp #knapsack

            0-1 knapsack problem. DP: O(nW) time and O(W) space
        """

        # dp[i][j] denotes the max number of subset with at most i 0s and at most j 1s
        dp = [[0] * (n+1) for _ in range(m+1)]

        # formula: dp[i][j] = max(dp[i][j],dp[i-x][j-y]+1) for any str, where x,y is the number of 0s and 1s

        # dp traverse order: descending m and descending n. strs traverse order: any order
        # If a cell in the dp is updated (because word is selected), we should be adding 1 to dp[i][j] from the previous iteration (when we were not considering word)
        # If we go from top left to bottom right, we would be using results from this iteration => overcounting
        for word in strs:
            x = word.count("0")
            y = len(word) - x
            for i in range(m,x-1,-1):
                for j in range(n,y-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-x][j-y]+1)
        return dp[m][n]