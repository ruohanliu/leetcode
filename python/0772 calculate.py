class Solution:
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
        stack = []
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
            elif x == "(":
                stack.append((l1,o1,l2,o2))
                l1 = 0
                o1 = l2 = o2 = 1
            elif x == ")":
                num = l1 + o1 * l2
                l1,o1,l2,o2 = stack.pop()

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