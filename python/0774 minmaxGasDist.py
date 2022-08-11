from typing import List
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """
            #binarysearch #float
        """
        def check(limit):
            quantity = 0
            for distance,c in count:
                q,m = divmod(distance,limit)
                quantity += (q - (1 if m < precision else 0)) * c
                if quantity > k:
                    return False
            return True

        lo = 0
        hi = stations[-1] - stations[0]
        precision = 1e-6
        while hi - lo > precision:
            mid = (lo+hi) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return lo
            
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        lo = 0
        hi = stations[-1] - stations[0]
        precision = 1e-6
        count = Counter(y-x for x,y in zip(stations,stations[1:]))
        count = sorted([(d,count[d]) for d in count], reverse = True)
        while hi - lo > precision:
            mid = (lo+hi) / 2
            if sum(math.ceil(distance / mid) * c for distance,c in count) <= k:
                hi = mid
            else:
                lo = mid
        return lo