class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
            #dp #relation #important #subsequence

            related 828
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

        
    def distinctSubseqII(self, s):
        end = [0] * 26
        for c in s:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)

    def distinctSubseqII(self, s):
        end = [0] * 26
        ans = 0
        for c in s:
            end[ord(c) - ord('a')],ans = ans+1,2*ans+1-end[ord(c) - ord('a')]
        return ans % (10**9 + 7)