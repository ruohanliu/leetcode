class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
            #bitwise #important

            for two positive integer x > y 
            carry = (x&y) <<1
            borrow = ((~x)&y)<<1
        """
        x,y = abs(a), abs(b)
        if x<y:
            return self.getSum(b,a)
        
        sign = 1 if a > 0 else -1
        
        if a*b >= 0:
            while y:
                xor = x^y
                carry = (x&y) <<1
                x,y = xor,carry
        else:
            # compute x-y. x is bigger
            while y:
                xor = x^y
                borrow = ((~x) & y) << 1
                x,y = xor,borrow
        return x * sign
            
            