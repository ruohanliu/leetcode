class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
            #important #bitwise #inplace #shift #rotation
            when inplace rotate, save original info in the same slot to retrieve later
        """
        n = len(nums)
        for i,item in enumerate(nums):
            nums[i] += n*(nums[item]%n)
        for i,item in enumerate(nums):
            nums[i] //= n
        return nums
