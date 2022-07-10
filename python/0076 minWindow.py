class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            #slidingwindow #important
        """
        left = 0
        cs = Counter()
        ct = Counter(t)
        ans = ""
        need = len(t)
        have = 0
        for right in range(len(s)):
            r = s[right]
            cs[r]+=1
            if cs[r] <= ct[r]:
                have += 1
            while have == need:
                if not ans or (right-left+1) < len(ans):
                    ans = s[left:right+1]
                cs[s[left]]-=1
                if cs[s[left]] < ct[s[left]]:
                    have -= 1
                left += 1
        return ans