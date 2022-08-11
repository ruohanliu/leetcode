class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
            #binarysearch
            
            on nums[index]
        """
        def total(i,val):
            l = min(i,val-1)
            r = min(n-i-1,val-1)
            return val + (val-1 + max(val - l,1)) * l // 2 + (val-1 + max(val - r,0)) * r // 2 + i-l + n-i-1-r
            
        lo = 1
        hi = maxSum
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if total(index,mid) > maxSum:
                hi = mid - 1
            else:
                lo = mid
        return lo
