class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
            #dp #bottomuporder
        """
        @cache
        def dp(n,p,i):
            # invalid result should be filtered out first
            if n < 0:
                return 0
            if i == len(group) or n == 0:
                return 1 if p >= minProfit else 0
            return (dp(n-group[i],min(minProfit,p+profit[i]),i+1) + dp(n,p,i+1)) % mod
        mod = 10**9 + 7
        return dp(n,0,0)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit+1) for _ in range(n+1)]
        mod = 10**9 + 7
        # dp[i][j] count of schemes with exactly i members and j profit
        dp[0][0] = 1
        for g,p in zip(group,profit):
            for i in reversed(range(n-g+1)):
                for j in reversed(range(minProfit+1)):
                    dp[i+g][min(minProfit,j+p)] += dp[i][j]
        return sum(dp[x][minProfit] for x in range(n+1)) % mod