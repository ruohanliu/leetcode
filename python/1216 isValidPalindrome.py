class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
            #dp #palindrome
            
            related 1682 0516
        """
        @cache
        def dp(i,j):
            if i>j:
                return 0
            if i == j:
                return 1
            elif i+1 == j and s[i] == s[j]:
                return 2
            elif s[i] == s[j]:
                return 2 + dp(i+1,j-1)
            else:
                return max(dp(i+1,j),dp(i,j-1))

        n = len(s)
        ans = dp(0,n-1)
        dp.cache_clear()
        return ans + k >= n