from typing import List
from operator import add
from functools import reduce
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
            functools.reduce
            operator.add
        """
    
        n = len(nums)
        # dp[i] stores the sequences ending at i
        dp = [[[nums[i]]] for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] += [subsequence+[nums[i]] for subsequence in dp[j]]

        return set(tuple(x) for x in reduce(add,dp) if len(x) > 1)