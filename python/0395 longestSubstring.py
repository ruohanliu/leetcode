class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
            #slidingwindow #important
        """
        c = Counter(s)
        nUniqueChar = len(c)
        ans = 0
        for maxUniqueChar in range(1,nUniqueChar+1):
            c = Counter()
            lo = 0
            nK = 0
            for hi,char in enumerate(s):
                c[char] += 1
                if c[char] == k:
                    nK += 1
                while len(c) > maxUniqueChar:
                    if c[s[lo]] == 1:
                        del c[s[lo]]
                    else:
                        c[s[lo]] -= 1
                        if c[s[lo]] == k-1:
                            nK -= 1
                    lo += 1
                if len(c) == nK:
                    ans = max(ans,hi-lo+1)
        return ans