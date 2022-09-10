class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
            #slidingwindow
            related 1248
        """
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        c = {x:0 for x in "abc"}
        for x in s:
            c[x] += 1
            while all(c[k] for k in c):
                c[s[i]] -= 1
                i += 1
            ans += i
        return ans