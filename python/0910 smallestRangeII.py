class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        """
            #greedy
        """
        lo,hi = min(nums),max(nums)
        maxDiff = hi - lo
        if maxDiff >= 4*k:
            return maxDiff-2*k
        if maxDiff <= k:
            return maxDiff

        nums.sort()
        res = maxDiff
        right = nums[-1]-k
        left = nums[0]+k
        for i in range(len(nums) - 1):
            res = min(res, max(nums[i] + k,right) - min(nums[i+1] - k,left))
        return res