from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        l = len(nums)
        prod = 1
        for i in range(0,l-1):
            prod *= nums[i]
            left.append(prod)

        prod = 1
        for i in range(l-1,0,-1):
            prod *= nums[i]
            right.append(prod)

        return [right[-1-i] * left[i] for i in range(l)]

    def productExceptSelf_less_space(self, nums: List[int]) -> List[int]:
        """
        take-away
            when output array is not counted towards space complexity, we can use output array as cache

        use left as ans
        """
        left = [1]
        l = len(nums)
        prod = 1
        for i in range(0,l-1):
            prod *= nums[i]
            left.append(prod)

        prod = 1
        for i in range(l-1,-1,-1):
            left[i] *= prod
            prod *= nums[i]
        return left

s = Solution()
print(s.productExceptSelf_less_space([-1,1,0,-3,3]))
