class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
            #dp #palindrome
        """
        @cache
        def cost(i,j): #calculate the cost of transferring one substring into palindrome string
            ans = 0
            while i < j:
                if s[i] != s[j]:
                    ans += 1
                i += 1
                j -= 1
            return ans

        @cache
        def dp(i, k): 
            if n-i == k:
                return 0
            if k == 1:
                return cost(i,n-1)
            ans = float("inf")
            for j in range(i,n-k+1):
                ans = min(ans,cost(i,j) + dp(j+1,k-1))
            return ans
        
        n = len(s)
        return dp(0,k)