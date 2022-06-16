from typing import List
class Solution:
    def jump_dp(self, nums: List[int]) -> int:
        """
            #dp
        """
        n = len(nums)
        if n == 1:
            return 0
        # dp[i] denotes the min number of jumps to index i
        dp = [n] * len(nums)

        # initialization
        dp[0] = 0

        # dp traverse order: does not matter because dp[i+j] do not overlap with each other
        for i, num in enumerate(nums):
            maxReachable = i+num
            if maxReachable >= n-1:
                return dp[i] + 1
            for j in range(1, num+1):
                dp[i+j] = min(dp[i+j], dp[i]+1)

        return dp[-1]

    def jump_bfs(self, nums: List[int]) -> int:
        """
            #dp #bfs
            use bfs to avoid repeatedly visit an index
        """
        n = len(nums)
        if n == 1:
            return 0

        # dp[i] denotes the min number of jumps to index i
        dp = [n] * len(nums)

        # initialization
        dp[0] = 0

        bfs = [0]
        while bfs:
            bfs_next = []
            for i in bfs:
                maxReachable = i+nums[i]
                if maxReachable >= n-1:
                    return dp[i] + 1
                for j in range(i+1, i+nums[i]+1):
                    if dp[j] == n:
                        dp[j] = dp[i]+1
                        bfs_next.append(j)
            bfs = bfs_next

    def jump_step(self, nums: List[int]) -> int:
        """
            avoid dp and bfs because each iteration only increase step by 1, and reached index is monotonically increasing
        """
        n = len(nums)
        ans = l = r = 0
        while r < n - 1:
            maxReachable = r
            for i in range(l, r+1):
                maxReachable = max(maxReachable, i+nums[i])
            l = r+1
            r = maxReachable
            ans += 1
        return ans

    def jump_step(self, nums: List[int]) -> int:
        """
            also observe that each index is only visited once, so instead of iterate by step, we can also go over the nums
        """
        n = len(nums)
        ans = r = maxReachable = 0
        for i in range(n):
            if i > r:
                ans += 1
                r = maxReachable
            maxReachable = max(maxReachable, i+nums[i])
        return ans
