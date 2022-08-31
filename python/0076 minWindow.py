class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            #slidingwindow
        """
        i = 0
        cs = Counter()
        ct = Counter(t)
        ans = ""
        need = len(t)
        have = 0
        for j in range(len(s)):
            r = s[j]
            cs[r]+=1
            if cs[r] <= ct[r]:
                have += 1
            while have == need:
                if not ans or (j-i+1) < len(ans):
                    ans = s[i:j+1]
                cs[s[i]]-=1
                if cs[s[i]] < ct[s[i]]:
                    have -= 1
                i += 1
        return ans