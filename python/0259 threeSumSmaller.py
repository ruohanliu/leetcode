from typing import List
class Solution:
    """
        Use two pointer method, add diff (k-j) to result
    """
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums) - 2:
            # optimize
            if nums[i] * 3 >= target : break
            j = i + 1
            k = len(nums) - 1
            complement = target - nums[i]
            while j < k:
                if nums[j] + nums[k] < complement:
                    ans += k - j
                    j += 1
                else:
                    k -= 1
            i += 1
        return ans
s = Solution()
print(s.threeSumSmaller([-2,0,1,3],2))
