from typing import List
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """
            #binarysearch #float
        """

        def check(limit):
            quantity = 0
            for i in range(1,len(stations)):
                distance = stations[i] - stations[i-1]
                if distance % limit == 0:
                    quantity += distance // limit - 1
                else:
                    quantity += distance // limit

                if quantity > k:
                    return False

            return True

        lo = 1
        hi = stations[-1] - stations[0]
        while hi - lo > 10**(-6):
            mid = (lo+hi) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return lo
            