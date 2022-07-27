class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
            #recursion
        """
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i,c in enumerate(expression):
            if c in "-+*":
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i+1:])
                res.extend(eval(str(x)+c+str(y))for x in l for y in r)
        return res