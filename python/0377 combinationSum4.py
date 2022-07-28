class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
            #dp #permutation
            related 0518
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for amt in range(1,target+1):
            for num in nums:
                if amt - num >= 0:
                    dp[amt] += dp[amt-num]
        return dp[target]
