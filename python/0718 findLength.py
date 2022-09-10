from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #dp 
            Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

            similar to find longest common subsequence

            rolling hash (Rabin-Karp algorithm)
        """
        m = len(nums1)
        n = len(nums2)

        curr = [0] * (n+1)
        prev = [0] * (n+1)

        ans = 0

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    curr[j+1] = prev[j] + 1
                    ans = max(curr[j+1], ans)
                else:
                    curr[j+1] = 0
            curr, prev = prev, curr
        return ans

    def findLength_tle(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i,j):
            nonlocal ans
            if i == 0 or j == 0:
                return 0

            dp(i-1,j)
            dp(i,j-1)
            if nums1[i-1] == nums2[j-1]:
                res = dp(i-1,j-1) + 1
                ans = max(ans,res)
                return res
            else:
                return 0
            
        m = len(nums1)
        n = len(nums2)
        ans = 0
        dp(m,n)
        return ans