from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
            #monostack

            circular list requires 2 passes. At the end of 2 passes, no need to consider what's left in the stack if ans array is initialized with -1
        """
        n = len(nums)
        ans = [-1] * n
        # stores the indices
        monoStack = []
        for i in range(n*2):
            while monoStack and nums[monoStack[-1]] < nums[i % n]:
                ans[monoStack.pop()] = nums[i % n]
            monoStack.append(i % n)
        return ans

