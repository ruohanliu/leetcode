class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            #dp #palindrome #string #furtherstudy
            O(N^2)

            Optimally, the problem can be solved in O(nlogn) time
            https://leetcode.com/problems/palindromic-substrings/solution/
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n-1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += dp[i][j]
        return ans

    def countSubstrings(self, s: str) -> int:
        """
            Construct palindrome for the center
            O(N^2)
        """
        n = len(s)
        ans = n
        for i in range(n):
            j = 1
            while i-j >= 0 and i+j <= n-1 and s[i-j] == s[i+j]:
                ans += 1
                j += 1

        for i in range(n-1):
            if s[i] != s[i+1]:
                continue
            ans += 1
            j = 1
            while i-j >= 0 and i+1+j <= n-1 and s[i-j] == s[i+1+j]:
                ans += 1
                j += 1
        return ans
