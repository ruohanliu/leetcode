from bisect import bisect_left
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            #binarysearch
        """
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if nums[-1] > nums[0]:
            k = bisect_left(nums, target)
            if k >= n or nums[k] != target:
                return -1
            else:
                return k

        lo = 0
        hi = n-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if nums[mid] > nums[-1]:
                lo = mid
            else:
                hi = mid-1
        rotate = hi

        print(rotate)

        if target > nums[-1]:
            k = bisect_left(nums, target, 0, rotate+1)
            if k > rotate or nums[k] != target:
                return -1
            else:
                return k
        else:
            k = bisect_left(nums, target, rotate+1, n)
            if k >= n or nums[k] != target:
                return -1
            else:
                return k
