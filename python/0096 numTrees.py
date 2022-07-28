class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            total = 0
            for j in range(1,i+1):
                total += dp[j-1]*dp[i-j]
            dp[i] = total
        return dp[-1]
            
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        return sum(self.numTrees(j-1)*self.numTrees(n-j) for j in range(1,n+1))
