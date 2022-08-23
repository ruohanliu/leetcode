class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
            #dp #LIS #important
            related: 300
        """
        # dp[i] stores the LIS ending at i (length,freq)
        n = len(nums)
        dp = [[1,1] for _ in range(n)]
        globalMax = 1
        for i in range(1,n):
            localMax = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j][0]+1 > localMax:
                        localMax = dp[j][0]+1
                        dp[i] = [localMax,dp[j][1]]
                    elif dp[j][0]+1 == localMax:
                        dp[i][1] += dp[j][1]
            globalMax = max(globalMax,localMax)
        return sum(f for l,f in dp if l == globalMax)