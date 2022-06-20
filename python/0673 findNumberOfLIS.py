class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
            #dp #LIS
            related: 300
        """
        # dp[i] stores the LIS ending at i
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]

        currMax = 0
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j][0]+1 > dp[i][0]:
                        dp[i] = [dp[j][0]+1, 1]
                    elif dp[j][0]+1 == dp[i][0]:
                        dp[i][1] += 1
            currMax = max(currMax, dp[i][1])
        return sum(x[1] for x in dp if x[1] == currMax)
