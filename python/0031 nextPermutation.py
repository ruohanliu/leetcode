from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
            bisect does not work with descending order list
            #binarysearch #permutation #important

            because of pass by assignment, reverse an argument nums cannot use
            `nums = nums[::-1]`
            instead, use
            `nums[] = nums[::-1]`
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                lo = i
                hi = len(nums)-1
                mid = lo
                while lo < hi:
                    mid = (lo+hi) // 2 + 1
                    if nums[mid] > nums[i-1]:
                        lo = mid
                    else:
                        hi = mid - 1

                nums[i-1], nums[hi] = nums[hi], nums[i-1]
                nums[i:] = nums[i:][::-1]
                return
        nums[::] = nums[::-1]
