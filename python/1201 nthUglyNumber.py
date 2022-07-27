class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
            #math #gcd #binarysearch
        """
        from math import gcd
        ab = gcd(a,b)
        ac = gcd(a,c)
        bc = gcd(b,c)
        abc = gcd(ab,c)

        def enough(k):
            res = k//a + k//b + k//c + k//ab + k//ac + k//bc + k//abc
            return res >= n

        lo = 1
        hi = 10**9
        while lo < hi:
            mid = (lo+hi) // 2
            if enough(mid):
                hi = mid
            else:
                lo = mid+1
        return mid
