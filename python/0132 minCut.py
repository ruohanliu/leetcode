class Solution:
    def minCut(self, s: str) -> int:
        """
            #dp #palindrome
        """
        def isPalindrome(i,j):
            return j == i+1 or s[i:j] == s[i:j][::-1]
        
        @cache
        def minCut(i,j):
            if isPalindrome(i,j):
                return 1
            
            ans = float("inf")
            for k in range(i+1,j):
                if isPalindrome(i,k):
                    ans = min(ans,1+minCut(k,j))
            return ans

        return minCut(0,len(s))-1
