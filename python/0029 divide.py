class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
            #math #digits
        """
        if (dividend == -2**31 and divisor == -1):
            return 2**31-1
        sign = (dividend > 0) == (divisor > 0)
        a, b, res = abs(dividend), abs(divisor), 0
        for x in reversed(range(32)):
            if a >= b << x:
                res += 1 << x
                a -= b << x
        return res if sign else -res