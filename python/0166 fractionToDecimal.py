class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
            #math #division
        """
        sign = '-' if numerator*denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        n, remainder = divmod(numerator, denominator)

        ans = [sign+str(n), '.']
        seen = {}
        while remainder and remainder not in seen:
            seen[remainder] = len(ans)
            n, remainder = divmod(remainder*10, denominator)
            ans.append(str(n))

        if remainder:
            ans.insert(seen[remainder], '(')
            ans.append(')')
        return ''.join(ans).rstrip('.')