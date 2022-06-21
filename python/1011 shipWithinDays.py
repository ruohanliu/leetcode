from bisect import bisect_right
from itertools import accumulate
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
            #binarysearch
        """
        def check(limit):
            ans = 0
            lo = 0
            lastPrefixSum = 0
            while lo < n:
                lo = bisect_right(prefixSum,limit,lo)
                ans += 1
                limit += prefixSum[lo-1] - lastPrefixSum
                lastPrefixSum = prefixSum[lo-1]
                if ans > days:
                    return False
            return True

        n = len(weights)
        lo,hi = max(weights),sum(weights)
        prefixSum = list(accumulate(weights))
        
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid+1
        return lo