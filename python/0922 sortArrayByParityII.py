class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
            #inplace #shift
        """
        o = 1
        e = 0
        while True:
            while nums[e] & 1 == 1:
                while nums[o] & 1 == 1:
                    o += 2
                nums[o], nums[e] = nums[e], nums[o]
                o += 2
            e += 2
            if e == len(nums) or o > len(nums):
                return nums
