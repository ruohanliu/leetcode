from math import perm
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """
            #digits
            related: 1012
        """
        L = list(map(int,str(n+1)))
        ans = 0
        m = len(L)
        seen = set()
        for i in range(1,m):
            ans += 9 * perm(9,i-1)
        for i,x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in seen:
                    ans += perm(9-i,m-i-1)
            if x in seen:
                break
            seen.add(x)
        return ans