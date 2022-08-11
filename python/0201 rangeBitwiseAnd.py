class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
            #bitwise
            
            related 1521
            when m != n, There is at least an odd number and an even number, so the last bit position result is 0
        """
        while left < right:
            right = right & (right - 1)
            
        return right & left

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # find the common 1-bits
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift