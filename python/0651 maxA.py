class Solution:
    def maxA(self, n: int) -> int:
        """
            #dp #relation
        """
        @cache
        def dp(n,curr,pasted):
            if n == 0:
                return curr
            if n < 0:
                return float("-inf")
            if curr == 0:
                if n <= 6:
                    return n
                else:
                    return max(dp(n-6,6,3),dp(n-6,4,4))
            return max(dp(n-3,curr*2,curr),dp(n-1,curr+pasted,pasted))
            
        return dp(n,0,0)

    @cache
    def maxA(self, n: int) -> int:
        if n <= 6:
            return n
        return max(self.maxA(n-3)*2,self.maxA(n-4)*3,self.maxA(n-5)*4)
        
    def maxA(self, n: int) -> int:
        """
            3-5keys ~ 3 choices
            6 keys has 2 choices but it is covered by previous 3 keys
        """
        dp = [0]*(n+1)
        for i in range(min(7,n+1)):
            dp[i] = i
        for i in range(7,n+1):
            dp[i] = max(dp[i-3]*2,dp[i-4]*3,dp[i-5]*4)
                
        return dp[n]