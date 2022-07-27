class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        """
            #dp
        """
        @cache
        def dp(n):
            if n <= 2:
                return 1
            ans = 0
            for i in range(0,n,2):
                ans += dp(i) * dp(n-i-2)
            return ans % mod
        mod = 10**9 + 7
        return dp(numPeople)