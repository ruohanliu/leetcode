class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
            #dp #relation #important #subsequence
        """
        dp = [1]
        last = {}
        for i,c in enumerate(s):
            # use or not use
            dp.append(dp[-1] * 2)
            # if c appearred before, subtract the result ending before last c
            if c in last:
                dp[-1] -= dp[last[c]-1]
            last[c] = [i+1]
        return (dp[-1] - 1) % (10 ** 9 + 7)

        
