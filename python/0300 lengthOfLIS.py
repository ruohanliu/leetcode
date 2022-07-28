from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            #dp #lis

            dp[i] usually stores the result for sequence that ends at i
        """

        # dp[i] stores the LIS ending at i
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)

    def lengthOfLIS_rec(self, nums: List[int]) -> int:
        """
            #recursion
            every possible call of the recursion function must be made
        """
        from functools import cache
        @cache
        def lis(i):
            nonlocal res
            if i == 0:
                return 1
            recMax = 1
            for j in range(i):
                # Must calculate lis(j) regardless
                recRes = lis(j)
                if nums[i] > nums[j]:
                    recMax = max(recMax, recRes+1)
 
            res = max(res, recMax)
            return recMax

        res = 1
        lis(len(nums)-1)
        return res

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            #simulation #binarysearch #important
            the end res list may not contain the correct subsequence but its length is the correct answer to the problem
        """
        from bisect import bisect_left
        n = len(nums)
        res = [nums[0]]

        for i in range(1, n):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                res[bisect_left(res,nums[i])] = nums[i]
        return len(res)
