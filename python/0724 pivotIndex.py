from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_total = sum(nums)
        left_total = 0
        for i in range(len(nums)):
            if i > 0:
                left_total += nums[i-1]
            right_total -= nums[i]
            if left_total == right_total:
                return i
        return -1
