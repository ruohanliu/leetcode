class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            #backtrack
        """
        res = []
        stack = []
        
        def backtrack(openN, closedN):
        ans = []
        progress = []
        
        def backtrack(l,r):
            if l == r == n:
                ans.append("".join(progress))
            if l<n:
                progress.append("(")
                backtrack(l+1,r)
                progress.pop()
            if r<l:
                progress.append(")")
                backtrack(l,r+1)
                progress.pop()
        
        backtrack(0,0)
        return ans
            
            

    @cache
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for m in range(n):
            for left in self.generateParenthesis(m):
                for right in self.generateParenthesis(n-m-1):
                    ans.append(f"({left}){right}")
        return ans