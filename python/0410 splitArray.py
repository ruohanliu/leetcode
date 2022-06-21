from bisect import bisect_right
from itertools import accumulate
from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
            #binarysearch #prefixsum

            each split result in sum LE limit, use bisect_right
        """
        def check(limit):
            ans = 0
            lo = 0
            lastPrefixSum = 0
            while lo < n:
                lo = bisect_right(prefixSum, limit, lo)
                ans += 1
                limit += prefixSum[lo-1] - lastPrefixSum
                lastPrefixSum = prefixSum[lo-1]
                if ans > m:
                    return False
            return True

        n = len(nums)
        lo, hi = nums[0], sum(nums)
        prefixSum = list(accumulate(nums))

        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid+1
        return lo
