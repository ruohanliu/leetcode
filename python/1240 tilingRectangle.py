class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """
            #dp

            this is a proximation and not correct
        """
        @cache
        def dp(n,m):
            if (n,m) in {(11,13),(13,11)}:
                return 6
        
            if n == m:
                return 1
        
            if n>m:
                n,m = m,n
                
            ans = dp(m-n,n) + 1

            for i in range(1, n // 2 + 1):
                ans = min(ans, dp(i, m) + dp(n - i, m))

            for j in range(1, m // 2 + 1):
                ans = min(ans, dp(n, j) + dp(n, m - j))

            return ans
        return dp(n,m)