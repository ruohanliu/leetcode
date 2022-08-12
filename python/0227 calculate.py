class Solution:
    """
        #design
    """
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        num = 0
        sign = "+"
        stack = []
        for i,x in enumerate(s):
            if x.isdigit():
                num = num * 10 + int(x)
            if (not x.isdigit() and not x.isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    q,m = divmod(stack.pop(),num)
                    if q<0 and m != 0:
                        stack.append(q+1)
                    else:
                        stack.append(q)
                
                sign = x
                num = 0
        return sum(stack)