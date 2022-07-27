# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
            #binarysearch
        """

        n = mountain_arr.length()
        lo = 0
        hi = n-1
        while lo < hi:
            mid = (lo+hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                lo = mid+1
            else:
                hi = mid
        peak = lo

        if mountain_arr.get(peak) == target:
            return peak
        elif mountain_arr.get(peak) < target:
            return -1

        lo = 0
        hi = peak
        while lo <= hi:
            mid = (lo+hi)//2
            if mountain_arr.get(mid) > target:
                hi = mid-1
            elif mountain_arr.get(mid) < target:
                lo = mid+1
            else:
                return mid

        lo = peak
        hi = n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if mountain_arr.get(mid) < target:
                hi = mid-1
            elif mountain_arr.get(mid) > target:
                lo = mid+1
            else:
                return mid
        return -1
