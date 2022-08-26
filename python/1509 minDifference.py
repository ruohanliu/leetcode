class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def helper(nums,k):
            if not nums:
                return 0
            if k == 0:
                return nums[-1] - nums[0]
            return min(helper(nums[1:],k-1),helper(nums[:-1],k-1))
        nums.sort()
        return helper(nums,3)

    def minDifference(self, A):
        return min(a - b for a,b in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))