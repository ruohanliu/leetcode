class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
            #bisect #binarysearch
        """
        arr2.sort()
        return sum([bisect.bisect_left(arr2,n-d) == bisect.bisect_right(arr2,n+d) for n in arr1])
