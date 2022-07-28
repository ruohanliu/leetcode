class Solution:
    def numTilings(self, n: int) -> int:
        """
            #dp
        """
        @cache
        def total(n):
            total = 0
            for k in range(3,n+1,2):
                total += dp(n-k) * 2
            for k in range(4,n+1,2):
                total += dp(n-k) * 2
            return total % mod

        @cache
        def dp(n):
            if n <= 1:
                return 1
            if n == 2:
                return 2
            return (dp(n-1) + dp(n-2) + total(n)) % mod
        mod = 10**9 + 7
        return dp(n)

    def numTilings(self, n: int) -> int:
        @cache
        def dp(n):
            if n <= 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 5
            return (dp(n-1)*2 + dp(n-3)) % mod
        mod = 10**9 + 7
        return dp(n)