class Solution:
    def balancedString(self, s: str) -> int:
        """
            #slidingwindow
        """
        n = ans = len(s)
        t = n // 4
        c = Counter(s)
        i = 0
        for j,x in enumerate(s):
            c[x] -= 1
            while i<n and max(c[k] for k in c) <= t:
                ans = min(ans,j-i+1)
                c[s[i]] += 1
                i+=1
        return ans