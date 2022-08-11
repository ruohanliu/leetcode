class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """
            #dp #math #permutation #important #digit

            related: 1067

            example: 8765
            XXX
            XX
            X
            1XXX ~ 7XXX
            80XX ~ 86XX
            870X ~ 875X
            8760 ~ 8765
        """
        # number of ways to select n balls out of n balls
        @cache
        def A(m,n):
            return 1 if n == 0 else A(m,n-1) * (m-n+1)
        
        @cache
        def A(m,n):
            ans = 1
            for _ in range(n):
                ans *= m
                m -= 1
            return ans

        L = list(map(int,str(n+1)))
        m = len(L)
        ans = 0
        seen = set()
        for i in range(1,m):
            ans += 9 * A(9,i-1)
        for i,x in enumerate(L):
            for y in range(0 if i else 1,x):
                if y not in seen:
                    ans += A(9-i,m-i-1)
            # if repeated digits, after processing, stop for the less significant digits
            if x in seen:
                break
            seen.add(x)

        return n-ans
