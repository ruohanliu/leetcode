from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            ans = 0
            for p in piles:
                ans += int(math.ceil(p/k))
                if ans > h:
                    return False
            return True
        
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo+hi) //2
            if check(mid):
                hi = mid
            else:
                lo = mid+1
        return lo