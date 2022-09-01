class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        """
            #monostack #important #clever
        """
        dp = nums[:]
        ans = []
        n = len(nums)
        for size in range(n):
            mx = 0
            for i in range(n-size):
                curr = min(dp[i],nums[i+size])
                dp[i] = curr
                mx = max(mx,curr)
            ans.append(mx)
        return ans