class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
            #google #arithmetic
        """
        dp = defaultdict(lambda:1)
        n = len(nums)
        for j in range(1,n):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[j,diff] = dp[i,diff] + 1
        return max(dp.values())