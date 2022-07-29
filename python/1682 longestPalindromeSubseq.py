class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
            #dp
            cache_clear()
            
            related 0516 1216
        """
        @cache
        def dp(i,j,curr):
            if i>=j:
                return 0
            if s[i] == s[j] and s[i] != curr:
                return 2 + dp(i+1,j-1,s[i])
            else:
                return max(dp(i+1,j,curr),dp(i,j-1,curr))

        n = len(s)
        ans = dp(0,n-1,"")
        dp.cache_clear()
        return ans