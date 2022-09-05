class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            #dp #Manacher #algorithm #palindrome
        """
        def check(l, r):
            while 0 <= l and r < n and s[l] == s[r]: 
                l -= 1
                r += 1
            return l+1, r-1

        n = len(s)
        L = R = 0
        for i in range(n-1):
            l,r = check(i,i)
            l2,r2 = check(i,i+1) if s[i] == s[i+1] else (0,0)
            if r-l > R-L:
                L,R = l,r
            if r2-l2 > R-L:
                L,R = l2,r2
        return s[L:R+1]

    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans

    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        n, l, r = len(s), 0, 0
        dp = [[True]*n, [False]*n]    # dp[0]: old letters palindromes, dp[1]: even letters palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[1][i] = True
                l, r = i, i+1                        
        for m in range(2, n):         # m letters palindromes
            for i in range(n-m):
                j = i+m
                x, k = m%2, i+m//2
                dp[x][k] = dp[x][k] and s[i] == s[j]
                if dp[x][k] and j-i > r-l:
                    l, r = i, j
        return s[l:r+1]

    def longestPalindrome(self, s: str) -> str:
        t = '^#'+'#'.join(s)+'#$'
        n = len(t)
        p = [0]*n
        c = r = cm = rm = 0
        for i in range (1, n-1):
            p[i] = min(r-i, p[2*c-i]) if r > i else 0
            while t[i-p[i]-1] == t[i+p[i]+1]: p[i] += 1
            if p[i]+i > r: c, r = i, p[i]+i
            if p[i] > rm: cm, rm = i, p[i]
        return s[(cm-rm)//2:(cm+rm)//2]