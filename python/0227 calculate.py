class Solution:
    """
        #
    """
    def calculate(self, s: str) -> int:
        def operate(a,b,op):
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            else:
                return a//b
            
        ans = 0
        stack = deque()
        i = 0
        number = []
        while i < len(s):
            if not s[i].isdigit():
                if s[i] in "+-/*":
                    stack.append(s[i])
                i += 1
            else:
                while i < len(s) and s[i].isdigit():
                    number.append(s[i])
                    i+=1
                b = int("".join(number))
                number.clear()
                if stack and stack[-1] in "/*":
                    op = stack.pop()
                    a = stack.pop()
                    b = operate(a,b,op)
                stack.append(b)

                while len(stack) >= 4:
                    if str(stack[0]) in "+-":
                        op = stack.popleft()
                        if op == "-":
                            stack[0] *= -1
                    else:
                        a = stack.popleft()
                        op = stack.popleft()
                        stack[0] = operate(a,stack[0],op)
        if len(stack) == 1:
            return stack[0]
        elif len(stack) == 2:
            return operate(0,stack[0],stack[1])
        else:
            return operate(stack[0],stack[2],stack[1])
