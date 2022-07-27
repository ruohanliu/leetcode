from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            #rotation
        """
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] >0:
                if nums[i] == nums[nums[i]-1]:
                    nums[i] = 0
                    break
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        return [i+1 for i in range(len(nums)) if nums[i]==0]

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))