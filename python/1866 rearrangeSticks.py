class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
            #dp #relation
            related 1420
        """
        @cache
        def dp(n,v):
            # if all are visible
            if v == n:
                return 1
            # impossible
            if v == 0:
                return 0
            # cases for n is longest + cases for n is not longest
            # when n is not longest, it can always be rearranged to be invisible
            return (dp(n-1,v-1) + dp(n-1,v) * (n-1)) % mod
        mod = 10 ** 9 + 7
        return dp(n,k)
                