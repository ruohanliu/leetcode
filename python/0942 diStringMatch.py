class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = len(s)
        ans = []
        for c in s:
            if c == "I":
                ans.append(lo)
                lo +=1
            else:
                ans.append(hi)
                hi -= 1
        return ans+[hi]

    def diStringMatch(self, s: str) -> List[int]:
        """
            #greedy
        """
        c = Counter(s)
        p = len(s) - c["I"]
        ans = [p]
        if s[0] == "I":
            p += 1
            ans.append(p)
        else:
            p -= 1
            ans.append(p)
        n = 2
        for i in range(1,len(s)):
            if s[i] == "I":
                if s[i] == s[i-1]:
                    p += 1
                else:
                    p += n
            else:
                if s[i] == s[i-1]:
                    p -= 1
                else:
                    p -= n
            n += 1
            ans.append(p)
        return ans
            
        