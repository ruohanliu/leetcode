from bisect import bisect_left
from itertools import accumulate
from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
            #binarysearch 
        """
        def check(divisor):
            currSum = 0
            for x in nums:
                currSum += math.ceil(x / divisor)
                if currSum > threshold:
                    return False
            return True

        lo, hi = 1, max(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
