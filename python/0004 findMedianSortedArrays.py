from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).

        """

        """
        This is a selection problem. Equivalent to computing the average of (m+n+1)/2-th and (m+n+2)/2-th elements
        """

        def findKth(i, j, k):
            # helper function find Kth element after i and j
            # Kth element is 0-based
            if i >= m:
                return nums2[j + k - 1]
            if j >= n:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            # min inc is 1
            inc = k//2
            # Consider current i/j
            # At least one array has enough items
            # If a array does not have enough, use the other array
            midVal1 = nums1[i + inc - 1] if i + inc - 1 < m else float('inf')
            midVal2 = nums2[j + inc - 1] if j + inc - 1 < n else float('inf')
            
            if midVal1 < midVal2:
                return findKth(i + inc, j, k - k // 2)
            else:
                return findKth(i, j + inc, k - k // 2)

        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2

        return (findKth(0, 0, left) + findKth(0, 0, right)) / 2

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2, 7]))