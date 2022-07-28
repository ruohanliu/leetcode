class Solution:
    def wiggleSort_naive(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(2,len(nums),2):
            nums[i-1],nums[i] = nums[i],nums[i-1]
        
    def wiggleSort(self, nums: List[int]) -> None:
        """
            Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
        """
        increase = True
        for i in range(len(nums)-1):
            if (increase and nums[i+1]<nums[i]) or (not increase and nums[i+1]>nums[i]):
                nums[i],nums[i+1] = nums[i+1],nums[i]
            increase ^= True
