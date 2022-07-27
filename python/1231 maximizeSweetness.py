from bisect import bisect_left
from itertools import accumulate
from typing import List
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
            #binarysearch #bisect
            each split result in sum GE limit, use bisect_left
        """
        def check(limit):
            ans = 0
            nextCut = -1
            lastPrefixSum = 0
            while nextCut < n:
                nextCut = bisect_left(prefixSum, limit, nextCut+1)
                if nextCut < n:
                    ans += 1
                    limit += prefixSum[nextCut] - lastPrefixSum
                    lastPrefixSum = prefixSum[nextCut]

            return ans > k

        n = len(sweetness)
        lo, hi = 1, sum(sweetness)
        prefixSum = list(accumulate(sweetness))

        while lo < hi:
            mid = (lo + hi) // 2 + 1
            if check(mid):
                lo = mid
            else:
                hi = mid-1
        return lo
