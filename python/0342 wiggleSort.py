class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
            #furtherstudy #median #kth

            Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

            https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing
        """
        n = len(nums)
        nums.sort()
        half = (n+1)//2
        # must go from right to left
        nums[::2],nums[1::2] = nums[:half][::-1],nums[half:][::-1]