class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
            #math
        """
        ans = []
        seen = {}
        i = 0
        decimal = False
        negativesign = "-" if math.copysign(1,numerator) != math.copysign(1,denominator) else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        while True:
            if numerator == 0:
                break
            while numerator < denominator:
                numerator *= 10
                ans.append("0")
                i += 1
            if decimal:
                ans.pop()
                i-=1
                if numerator in seen:
                    break
                seen[numerator] = i
            q,m = divmod(numerator,denominator)
            ans.append(str(q))
            i+=1
            numerator = m
            decimal = True

        if numerator == 0:
            if not ans:
                return "0"
            elif len(ans) > 1:
                return negativesign+ans[0]+"."+"".join(ans[1:])
            else:
                return negativesign+ans[0]
        else:
            return negativesign+ans[0]+"."+"".join(ans[1:seen[numerator]]+["("]+ans[seen[numerator]:]+[")"])
            