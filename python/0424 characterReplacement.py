class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            #slidingwindow #important
            related 1004
        """
        c = Counter(s)
        ans = 0
        for a in c:
            i = 0
            _k = k
            for j,x in enumerate(s):
                if x != a:
                    _k -= 1
                if _k < 0:
                    if s[i] != a:
                        _k+=1
                    i+=1
            ans = max(ans,j-i+1)
        return ans
    
    def characterReplacement(self, s: str, k: int) -> int:
        c, i, ans = defaultdict(int), 0, 0
        for j,x in enumerate(s):
            c[x] += 1
            while i<j and j-i+1-max(c.values())>k:
                c[s[i]] -= 1
                i += 1
            ans = max(ans,j-i+1)
        return ans

    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = i = 0
        c = Counter()
        for j in range(len(s)):
            c[s[j]] += 1
            maxFreq = max(maxFreq, c[s[j]])
            if j - i + 1 - maxFreq > k:
                c[s[i]] -= 1
                i += 1
        return len(s) - i