class Solution:
    @cache
    def waysToDistribute_mle(self, n: int, k: int) -> int:
        """
            #dp #relation

            for n-th candy:
                it can go into any of the previous bag: fn(n-1,k) * k
                it can go into its own bag: fn(n-1,k-1) 
        """
        if n == k or k == 1:
            return 1
        mod = 10**9 + 7
        return (self.waysToDistribute(n-1,k) * k + self.waysToDistribute(n-1,k-1)) % mod

    
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(k+1):
            dp[i][i] = 1
        for i in range(n+1):
            dp[i][1] = 1
        for i in range(3,n+1):
            for j in range(2,k+1):
                dp[i][j] = (dp[i-1][j] * j + dp[i-1][j-1]) % mod
        return dp[n][k]