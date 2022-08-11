class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
            #dp #relation #bottomuporder

            instead of choosing the ballon to burst first, choose the one to burst last
        """
        # dp[i][j] is the max coins between i and j baloons
        nums = [1] + [x for x in nums if x != 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # smaller result dp[lo][i] and dp[i][hi] must be calculated before dp[lo][hi], therefore iterate from smaller k
        for k in range(2,n):
            for lo in range(n-k):
                hi = lo+k
                dp[lo][hi] = max(dp[lo][hi],max(nums[lo]*nums[i]*nums[hi] + dp[lo][i] + dp[i][hi] for i in range(lo+1,hi)))
        return dp[0][n-1]

    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(lo,hi):
            ans = 0
            for i in range(lo+1,hi):
                ans = max(ans,nums[i]*nums[lo]*nums[hi] + dp(lo,i) + dp(i,hi))
            return ans

        nums = [1] + [x for x in nums if x != 0] + [1]
        n = len(nums)
        return dp(0,n-1)