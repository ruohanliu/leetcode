class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
            #dp #math #relation
        """
        zeros = 0
        ones = 0
        mod = 10**9 +7
        for c in binary:
            if c == "1":
                ones = (zeros + ones + 1) % mod
            else:
                zeros = (zeros + ones) % mod
        ans = zeros + ones
        if binary.index("0") >= 0:
            ans += 1
        return ans