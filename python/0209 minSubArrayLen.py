from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            there are no negative value, therefore use sliding window

        """
        i = 0
        j = 0
        cumulative_sum = 0
        ans = float("inf")
        while j < len(nums):
            cumulative_sum += nums[j]
            while cumulative_sum >= target:
                ans = min(ans,j-i+1)
                cumulative_sum -= nums[i]
                i += 1
            j+=1

        return 0 if ans == float("inf") else ans
s = Solution()
print(s.minSubArrayLen(6,[10,2,3]))
