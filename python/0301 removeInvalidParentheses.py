from functools import cache
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
            #bfs #important
        """
        @cache
        def isValid(s):
            bal = 0
            for c in s:
                if c == "(":
                    bal +=1
                elif c==")":
                    bal -=1
                    if bal<0:
                        return False
            return bal == 0

        queue = {s}
        while queue:
            valid = list(filter(isValid,queue))
            if valid:
                return valid
            queue = {item[:i]+item[i+1:] for item in queue for i in range(len(item)) if item[i] in "()"}