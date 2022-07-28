class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
            #dp
        """
        n = len(nums)
        m = len(multipliers)
        # dp[i][j] stands for i-th move, j moves on the left side of nums
        dp = [[0] * (m+1) for _ in range(m+1)]
        for i in range(1,m+1):
            mult = multipliers[i-1]
            dp[i][0] = dp[i-1][0] + mult * nums[n-i]
            dp[i][i] = dp[i-1][i-1] + mult * nums[i-1]
            for left in range(1,i):
                dp[i][left] = max(dp[i-1][left] + mult * nums[n - (i - left)],dp[i-1][left-1] + mult * nums[left-1])
        return max(dp[-1])
                
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
            #dp #optimization
        """
        n = len(nums)
        m = len(multipliers)
        dp = [0] * (m+1)
        for i in range(1,m+1):
            mult = multipliers[i-1]
            dp[i] = dp[i-1] + mult * nums[i-1]
            for left in reversed(range(1,i)):
                dp[left] = max(dp[left] + mult * nums[n - (i - left)],dp[left-1] + mult * nums[left-1])
            dp[0] = dp[0] + mult * nums[n-i]
        return max(dp)