class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
            #dp #relation #arithmetic
        """
        n = len(nums)
        if n == 2:
            return 0
        ans = 0
        # dp[i][k] number of weak arithmetic subsequence with common diff k and ending at i
        dp = [defaultdict(int) for _ in range(n)]
        for j in range(n):
            for i in range(j):
                diff = nums[j]-nums[i]
                dp[j][diff] += dp[i][diff] + 1
                # for a given i and diff, number of weak arithmetic subsequence is 1 larger
                ans += dp[i][diff]
        return ans