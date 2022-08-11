from functools import cache
class Solution:
    dp = [0] * 32
    dp[0] = 1
    dp[1] = 2
    for i in range(2,32):
        dp[i] = dp[i-2] + dp[i-1]

    @cache
    def findIntegers(self, n: int) -> int:
        """
            #bitwise #dp #digit #relation
        """
        if n == 0:
            return 1
        if n == 1:
            return 2
        m = n.bit_length()
        ans = self.dp[m-1]
        n ^= 1<<(m-1)
        if m - 1 == n.bit_length():
            ans += self.dp[m-2]
        else:
            ans += self.findIntegers(n)
        return ans
