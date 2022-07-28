class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
            #rotation
            related 0448
        """
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] >0:
                if nums[i] == nums[nums[i]-1]:
                    nums[i] = -nums[i]
                    break
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        return [-nums[i] for i in range(len(nums)) if nums[i]<0]