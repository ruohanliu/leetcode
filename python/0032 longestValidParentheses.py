class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            #dp #parentheses #stack
        """
        n = len(s)
        dp = [0]*(n + 1)
        stack = []
        ans = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    # index of latest (
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
                    ans = max(ans,dp[i+1])
        return ans