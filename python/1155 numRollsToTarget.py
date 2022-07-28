class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
            #dp
        """
        @cache
        def dp(n,target):
            if n == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            return sum(dp(n-1,target-j) for j in range(1,k+1)) % mod
        
        if target < n or target > n*k:
            return 0
        mod = 10**9 + 7
        return dp(n,target)

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n*k:
            return 0
        mod = 10**9 + 7
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for t in range(target+1):
                dp[i][t] = sum(dp[i-1][t-j] for j in range(1,k+1) if t>=j) % mod

        return dp[n][target]
