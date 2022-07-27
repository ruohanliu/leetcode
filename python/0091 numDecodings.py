class Solution:
    def numDecodings(self, s: str) -> int:
        """
            #backtrack #dp #recursion
        """
        @cache
        def backtrack(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            ans = backtrack(i+1)
            if i<n-1 and s[i:i+2] <= "26":
                ans += backtrack(i+2)
            return ans
            
        n = len(s)
        return backtrack(0)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2,n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <=26:
                dp[i] += dp[i-2]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        """
            constant space
        """
        n = len(s)
        if s[0] == "0":
            return 0
        one = 1
        two = 1
        
        for i in range(1,n):
            res = 0
            if s[i] != "0":
                res += one
            if 10 <= int(s[i-1:i+1]) <=26:
                res += two
            one,two = res,one
        return one