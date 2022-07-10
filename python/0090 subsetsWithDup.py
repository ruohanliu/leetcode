class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        size = 0
        for i,x in enumerate(nums):
            startIndex = size if i>0 and nums[i] == nums[i-1] else 0 
            size = len(res)
            for j in range(startIndex,size):
                res.append(res[j]+[x])
        return res