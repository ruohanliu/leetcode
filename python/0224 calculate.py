class Solution:
    """
        #design
        related 227
    """
    def calculate_tle(self, s: str) -> int:
        """
            recursive solution is O(n^2)
        """
        if not s:
            return 0
        num = 0
        sign = "+"
        stack = []
        i = 0
        while i < len(s):
            x = s[i]
            if x.isdigit():
                num = num * 10 + int(x)
            if x == "(":
                bal = 1
                j = i + 1
                while bal:
                    if s[j] == "(":
                        bal += 1
                    elif s[j] == ")":
                        bal -= 1    
                    j += 1
                num = self.calculate(s[i+1:j-1])
                i = j-2
            elif (not x.isdigit() and not x.isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                
                sign = x
                num = 0
            i += 1
        return sum(stack)

    def calculate(self, s: str) -> int:
        """
            #design #hard

            +- is level 1 operation. l1 is the partial result. o1 == 1 for +, -1 for -
            */ is level 2 operation. l2 is the partial result. o2 == 1 for *, -1 for /

            evaluation: l1 = l1 + o1 * l2
        """
        # l1 o1 l2 o2 define state at any point
        l1 = 0
        o1 = l2 = o2 = 1
        i = 0
        n = len(s)
        while i < n:
            x = s[i]
            if x.isdigit():
                num = int(x)
                while i+1 < n and s[i+1].isdigit():
                    i += 1
                    num = num * 10 + int(s[i])
                
                # at end of a number, it is safe to update level 2 operand
                if o2 == 1:
                    l2 *= num
                else:
                    q,m = divmod(l2,num)
                    if q<0 and m != 0:
                        l2 = q + 1
                    else:
                        l2 = q
            elif x in "*/":
                o2 = 1 if x == "*" else -1
            # when at ) or +-, it is safe to evaluation level 1 operand
            elif x in "+-":
                l1 = l1 + o1 * l2
                o1 = 1 if x == "+" else -1
                
                l2 = o2 = 1
            
            i += 1
        return l1 + o1 * l2