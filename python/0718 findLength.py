from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #dp #furtherstudy 
            Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

            similar to find longest common subsequence

            rolling hash (Rabin-Karp algorithm)
        """
        m = len(nums1)
        n = len(nums2)

        curr = [0] * (n+1)
        prev = [0] * (n+1)

        ans = 0

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if nums1[i] == nums2[j]:
                    curr[j] = prev[j+1] + 1
                    ans = max(curr[j], ans)
                else:
                    curr[j] = 0
            curr, prev = prev, curr
        return ans
