class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
            #hammingdistance #bitwise

            take away
            bin(): convert integer to binary string prefixed with "0b"
            string.count()
            int.bit_count

            Bit Twiddling Hacks: http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
        """
        xor = x^y
        res = 0
        while xor > 0:
            xor,mod = divmod(xor,2)
            res += mod
        return res

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        res = 0
        while xor >0:
            res += 1
            xor = xor & (xor - 1)
        return res

    def hammingDistance(self, x: int, y: int) -> int:
        return (x^y).bit_count()

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")
            