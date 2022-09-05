class Solution:
    def checkRecord(self, n: int) -> int:
        """
            #dp #relation
            P-PL-PLL
        """
        @cache
        def dp(n):
            if n == 0:
                return 1
            elif n == 1:
                return 2
            elif n == 2:
                return 4
            elif n == 3:
                return 7
            else:
                return (2*dp(n-1)-dp(n-4)) % mod
            
        mod = 10**9+7
        # 0 absence
        ans = dp(n)
        # 1 absence
        for i in range(n):
            ans = (ans + dp(i) * dp(n-i-1)) % mod
        return ans