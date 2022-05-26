from typing import List
class Solution:
    """
    optimization:
        1. move pointer for duplicate adjacent numbers
        2. test first element * 3 value to trim

    take-away
        Unlike threeSum, 2nd and 3rd cannot increase and decrease at the same time.
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        ans = 0
        i = 0
        while i < len(nums) - 2:
            # optimize
            if nums[i] * 3 - target > diff: break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < diff:
                    ans = s
                    diff = abs(target - s)
                    if diff == 0:
                        return ans
                if s < target:
                    while j < len(nums) - 1 and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                else:
                    while k > i + 1 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
            i += 1
        return ans

s = Solution()
print(s.threeSumClosest([-1,0,1,1,55],3))
