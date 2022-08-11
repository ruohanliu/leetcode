from functools import cache


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
            #dp #bitmask
        """
        @cache
        def dp(i,state):
            if i == n:
                return 0

            ans = 0
            for j in range(2*n):
                for k in range(j+1,2*n):
                    if state & ((1 << j) + (1 << k)) == 0:
                        ans = max(ans,(i+1) * math.gcd(nums[j],nums[k]) + dp(i+1,state + (1<<j) + (1<<k)))
            return ans

        n = len(nums) // 2
        return dp(0,0)