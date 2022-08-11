class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
            #dp #combination #relation #important #math
            related 1866
        """
        # m stands for the max value in the array
        @cache
        def dp(n,m,k):
            # not enough distinct value to make k increases
            if m < k or k == 0:
                return 0

            # number of increase == numbers in the array
            if k == n:
                if n == m:
                    return 1
                # calculate c(m,n) with m must be in the selection
                # m could be in one of 1~n positions
                numerator = n
                denominator = 1
                for i in range(1,n):
                    numerator *= (m-i)
                for i in range(n):
                    denominator *= (i+1)
                return numerator // denominator % mod

            # there is no increase, keep using m, and number visible is still k
            ans = dp(n-1,m,k) * m
            # there is increase, sum all 1~(m-1)
            for j in range(1,m):
                ans += dp(n-1,j,k-1)
            return ans % mod
        
        mod = 10 ** 9 + 7
        return sum(dp(n,j,k) for j in range(1,1+m)) % mod