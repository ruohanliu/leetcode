class Solution:
    def mySqrt(self, x: int) -> int:
        """
            #math #binarysearch
        """
        lo = 0
        hi = x
        while lo<hi:
            mid = (lo+hi) // 2 + 1
            if mid*mid < x:
                lo = mid
            else:
                hi = mid - 1
        return lo

    def mySqrt(self, x: int) -> int:
        """
            #newton
        """
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r