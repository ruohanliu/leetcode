from itertools import accumulate
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
            #related 84
        """
        ps = list(accumulate(nums))
        nums.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(nums)):
            while nums[stack[-1]] > nums[i]:
                h = nums[stack.pop()]
                ans = max(ans, (ps[i-1] - (ps[stack[-1]] if stack[-1] != -1 else 0)) * h)
            stack.append(i)
        nums.pop()
        return ans % (10**9 +7)