from math import isqrt


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
            #rabin-karp
        """
        return s in (s*2)[1:-1]

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        t = n // 2
        for i in range(1,t+1):
            if n % i == 0:
                if s[:i]*(n//i-1) == s[i:]:
                    return True
                
        return False
            
    def repeatedSubstringPattern(self, s: str) -> bool:
        def checkHash(i,j):
            return (hashed[j] - hashed[i]*base[j-i]) % mod

        n = len(s)
        if n == 1:
            return False
        mod = 10**9+7
        base = [1]
        hashed = [0]

        for c in s:
            base.append(base[-1]*26%mod)
            hashed.append((hashed[-1]*26+ord(c)-97)%mod)

        for d in range(1,isqrt(n)+1):
            if n%d == 0:
                if d != 1 and d != n//d:
                    divisors = [d,n//d]
                else:
                    divisors = [d]
                for length in divisors:
                    h = checkHash(0,length)
                    if all(h == checkHash(length*(i+1),length*(i+2)) for i in range(n//length-1)):
                        return True
        return False