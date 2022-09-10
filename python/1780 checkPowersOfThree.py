class Solution:
    """
        #math
    """
    powersOf3 = [3 ** i for i in reversed(range(15))]
    def checkPowersOfThree(self, n: int) -> bool:
        for p in self.powersOf3:
            if n >= 2 * p:
                return False
            elif n >= p:
                n -= p
        return True