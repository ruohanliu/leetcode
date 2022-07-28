class Solution:
    def integerBreak(self, n: int) -> int:
        """
            #dp
        """
        dp = [i for i in range(59)]
        
        # it is always optimal to break intp 2 or 3 for n >= 5
        for i in range(5,n+1):
            dp[i] = max(dp[i-j]*dp[j] for j in (2,3))
            
        dp[2] = 1
        dp[3] = 2
        return dp[n]