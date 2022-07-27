# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
            #binarysearch

            when adjusting lo and hi, do not exclude potential valid index
        """
        lo = 1
        hi = n
        while lo < hi:
            m = (lo+hi)//2
            if isBadVersion(m):
                hi = m
            else:
                lo = m+1
        return lo
