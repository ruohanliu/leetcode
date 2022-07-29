class Solution:
    @cache
    def findDerangement(self, n: int) -> int:
        """
            #dp #relation

            swap n with one of the n-1 slots (say i)
            if i goes into n, then there are fn(n-2) options
            if i does not go into n, then there are fn(n-1) options
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        mod = 10**9 + 7
        return (self.findDerangement(n-1) + self.findDerangement(n-2))*(n-1) % mod

    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        a = 0
        b = 1
        mod = 10**9 + 7
        for i in range(3,n+1):
            a,b = b,(a+b)*(i-1) % mod
        return b