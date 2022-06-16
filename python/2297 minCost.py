from typing import List
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        """
            #dp #monostack
        """
        # dp[i] denotes the mincost jump to i
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0

        nextGreater = [-1] * n
        nextLess = [-1] * n

        greaterStack = []
        lessStack = []
        for i in range(n):
            while greaterStack and nums[greaterStack[-1]] <= nums[i]:
                nextGreater[greaterStack.pop()] = i
            while lessStack and nums[lessStack[-1]] > nums[i]:
                nextLess[lessStack.pop()] = i
            greaterStack.append(i)
            lessStack.append(i)

        for i in range(n):
            if nextGreater[i] > 0:
                dp[nextGreater[i]] = min(
                    dp[nextGreater[i]], dp[i]+costs[nextGreater[i]])
            if nextLess[i] > 0:
                dp[nextLess[i]] = min(
                    dp[nextLess[i]], dp[i]+costs[nextLess[i]])
        return dp[-1]