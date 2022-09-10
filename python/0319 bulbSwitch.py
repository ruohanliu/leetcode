class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
            #math
            only squares has odd number of divisors
            just count # of squares [1,n]
        """
        return math.isqrt(n)