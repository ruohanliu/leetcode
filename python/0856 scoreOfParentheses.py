import pstats


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
            #recursion #divideconquer #parentheses #important

            O(N^2)
        """
        def helper(lo,hi):
            balance = 0
            score = 0
            start = lo
            for i in range(lo,hi+1):
                if s[i] == "(":
                    balance += 1
                else:
                    balance -= 1
                if balance == 0:
                    if i - start == 1:
                        score += 1
                    else:
                        score += 2*helper(start+1,i-1)
                    start = i+1
            return score
        return helper(0,len(s)-1)

    def scoreOfParentheses(self, s: str) -> int:
        """
            add () values adjusted by balance
            O(N) time O(1) space
        """

        ans = 0
        balance = 0
        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            else:
                balance -= 1
                if s[i-1] == "(":
                    ans += 1 << balance
        return ans

    def scoreOfParentheses(self, s: str) -> int:
        """
            #stack
            O(N) time O(N) space
        """
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(score*2,1)
        return stack[0]
