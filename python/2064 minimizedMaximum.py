from typing import List
import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo,hi = 1,max(quantities)
        while lo < hi:
            mid = (lo+hi) //2
            if sum(math.ceil(q/mid) for q in quantities) <= n:
                hi = mid
            else:
                lo = mid+1
        return lo
