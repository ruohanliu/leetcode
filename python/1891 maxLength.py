from typing import List
from collections import Counter
class Solution:
    """
        #binarysearch
    """
    def maxLength(self, ribbons: List[int], k: int) -> int:
        c = Counter(ribbons)
        hi = sum([x*c[x] for x in c]) // k
        lo = 1
        
        def check(length):
            nonlocal c,k
            cnt = sum([x//length*c[x] for x in c])
            return cnt >= k
        
        while lo<hi:
            mid = (lo+hi) // 2 + 1
            if check(mid):
                lo = mid
            else:
                hi = mid-1
        return lo
s = Solution()
print(s.maxLength([7,5,9],4))