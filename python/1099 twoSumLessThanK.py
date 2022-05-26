from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        take away:
            if sorting is used, space complexity depends on the implementation of sorting algorithm
            O(n) or O(logn)
        """
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = float("-inf")
        while i < j:
            s = nums[i] + nums[j]
            if s >= k:
                j -= 1
            else:
                if s > ans:
                    ans = s
                i += 1
        return ans if ans > float("-inf") else -1


    def twoSumLessThanK_bisect(self, nums: List[int], k: int) -> int:
        """
        take away:
            from bisect import *
            bisect_left()
        """
        from bisect import bisect_left
        nums.sort()
        ans = float("-inf")
        for i in range(len(nums)):
            if nums[i] >= k: break
            j = bisect_left(nums,k - nums[i],i+1)
            if j-1>i:
                ans = max(ans,nums[j-1]+nums[i])
        return ans if ans > float("-inf") else -1

