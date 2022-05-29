from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
            use dict to store 1-0 count diff
        """
        diff = 0
        res = 0
        diff_dict = {0:-1}        
        for i in range(len(nums)):
            diff += 1 if nums[i] == 1 else - 1
            if diff in diff_dict:
                res = max(res,i-diff_dict[diff])
            else:
                diff_dict[diff] = i
        return res

s=Solution()
print(s.findMaxLength([0,0,1,0,0,0,1,1]))