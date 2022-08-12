from functools import cache
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """
            #dp #lcs #substring #binarysearch #rollinghash #rabin-karp #important #furtherstudy
            related 1044 1143
            
            O(n^2)
        """
        n = len(s)
        ans = 0
        dp = [[0] * n for _ in range(n+1)]
        for i in range(n):
            for j in range(i):
                if s[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ans = max(ans,dp[i+1][j+1])
            
        return ans

    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        prev = [0] * (n+1)
        curr = prev[:]
        for i in range(n):
            for j in range(i):
                if s[i] == s[j]:
                    curr[j+1] = prev[j] + 1
                    ans = max(ans,curr[j+1])
                else:
                    curr[j+1] = 0
            prev,curr = curr,prev
            
        return ans

    # print lcs longest common substring
    def lcs(s,t):
        n = len(s)
        m = len(t)
        prev = [0] * (n+1)
        curr = prev[:]
        r = ans = 0
        for i in range(m):
            for j in range(n):
                if s[j] == t[i]:
                    curr[j+1] = prev[j] + 1
                    if curr[j+1] > ans:
                        ans = curr[j+1]
                        r = j
                else:
                    curr[j+1] = 0
            prev,curr = curr,prev
        
        return s[r+1-ans:r+1]

    def longestRepeatingSubstring(self, s: str) -> str:
        """
            average O(nlogn) worst O(n^2)
        """
        def search(length):
            seen = set()
            for i in range(len(s)-length+1):
                substring = s[i:i+length]
                if substring in seen:
                    return True
                seen.add(substring)
            return False
            
        lo, hi = 0, len(s)-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if search(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def longestRepeatingSubstring(self, s: str) -> str:
        """
            O(nlogn)
        """
        def search(length):
            seen = set()
            for i in range(len(s)-length+1):
                val = (hashed[i+length] - hashed[i]*base[length]) % mod
                if val in seen:
                    return True
                seen.add(val)
            return False
            
        mod = 10**9+7
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
        return lo