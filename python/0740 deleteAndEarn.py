from collections import defaultdict
from functools import cache
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            #dp
        """
        n = len(nums)
        points = defaultdict(int)
        maxNum = 0
        for num in nums:
            points[num] += num
            maxNum = max(maxNum,num)

        dp = [0] * (n+1)
        dp[1] = points[1]
        for i in range(2,maxNum+1):
            dp[i] = max(dp[i]-dp[i-2],dp[i-1])

        return dp[maxNum]

    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            #memoization
        """
        points = defaultdict(int)
        maxNum = 0
        for num in nums:
            points[num] += num
            maxNum = max(maxNum,num)

        @cache
        def helper(i):
            if i == 0 :
                return 0
            if i == 1:
                return points[i]

            return max(points[i] + helper(i-2),helper(i-1))
        
        return helper(maxNum)