import heapq
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
            #binarysearch
        """
        def check(day):
            curr = 0
            ans = 0
            for d in bloomDay:
                if d <= day:
                    curr += 1
                    if curr == k:
                        curr = 0
                        ans += 1
                        if ans == m:
                            return True
                else:
                    curr = 0
            return False

            while lo < n:
                hi = bisect_right(bloomDay, day, lo)
                ans += (hi-lo) // k
                lo = hi+1
            print(day, ans, m)
            return ans >= m

        n = len(bloomDay)
        if m*k > n:
            return -1
        lo, hi = min(bloomDay), max(bloomDay)

        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid+1
        if check(lo):
            return lo
        else:
            return -1