class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
            #dp #relation
        """
        n = len(nums)
        if n == 2:
            return 0
        ans = 0
        # dp[i][k] number of weak arithmetic subsequence with common diff k and ending at i
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] += dp[j][diff] + 1
                ans += dp[j][diff]
        return ans