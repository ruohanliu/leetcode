from typing import List
class Solution:
    """
    Simple DP problem, only O(1) space complexity

    observation:
        a subarray of length >= 2's max product is non-negative (not useful)
        input numbers are all integer, there is not any float between 0 ~ 1, therefore
        the only way the abs of product can go down is when encountering a 0.

        O(1) space is enough to record the current max and min (negative max)

    take away:
        when slicing list, the end pointer can be len(nums)
    """
    def maxProduct_bf(self, nums: List[int]) -> int:
        """
        time limit exceed
        """
        from math import prod
        ans = float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                ans = max(prod(nums[i:j]),ans)

        return ans

    def maxProduct(self, nums: List[int]) -> int:
        """
        DP
        """
        last_max = nums[0]
        last_min = nums[0]

        ans = last_max
        for i in range(1,len(nums)):
            temp = last_max
            last_max = max(last_max*nums[i],last_min*nums[i],nums[i])
            last_min = min(temp*nums[i],last_min*nums[i],nums[i])
            ans = max(ans,last_max)

        return ans
s = Solution()
print(s.maxProduct_bf([-2]))


        