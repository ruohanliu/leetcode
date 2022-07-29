class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
            #rabin-karp #rollinghash #binarysearch

            #mersenne exponents: 2, 3, 5, 7, 13, 17, 19, 31, 61, 89... primes p such that 2^p-1 is prime

            related 1062
        """
        def search(length):
            nonlocal ans
            seen = set()
            for i in range(len(s)-length+1):
                val = (hashed[i+length] - hashed[i]*base[length]) % mod
                if val in seen:
                    ans = s[i:i+length]
                    return True
                seen.add(val)
            return False

        ans = ""       
        mod = 2**61-1
        base = [1]
        hashed = [0]
        for c in s:
            base.append(base[-1]*26%mod)
            hashed.append((hashed[-1]*26+ord(c)-97)%mod)

        lo, hi = 0, len(s)-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if search(mid):
                lo = mid
            else:
                hi = mid - 1
        return ans