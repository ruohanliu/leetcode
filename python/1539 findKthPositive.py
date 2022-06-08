from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
            #binarysearch
            // will round to the left
            prioritize increment on the left size while being careful not to exclude any valid value.
        """
        lo = 0
        hi = len(arr)-1
        
        if k > arr[hi]-hi-1:
            return k + hi + 1
        
        while lo < hi:
            mid = (lo+hi) // 2
            if arr[mid] - mid - 1 < k:
                lo = mid + 1
            else:
                hi = mid

        return k + hi
