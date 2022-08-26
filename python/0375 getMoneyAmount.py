class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
            #dp
            related 887
        """
        @cache
        def dp(lo,hi):
            if lo>=hi:
                return 0
            # no need to test hi
            return min(x+max(dp(lo,x-1),dp(x+1,hi)) for x in range(lo,hi))
        
        return dp(1,n)

    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n,0,-1):
            for hi in range(lo+1,n+1):
                dp[lo][hi] = min(x + max(dp[lo][x-1],dp[x+1][hi]) for x in range(lo,hi))
        return dp[1][n]