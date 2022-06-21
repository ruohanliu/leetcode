class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
            #math #dp

            while building towards nth ugly number, the kth ugly number must be used thrice by multiplying 2,3,5
            to form the next 3 numbers.

            it is possible that multiple candidates give the same next number, in which case move multiple pointers
        """
        dp = [1]
        p2,p3,p5 = 0,0,0
        c2,c3,c5 = 2,3,5
        for i in range(n-1):
            dp.append(min(c2,c3,c5))
            if dp[-1] == c2:
                p2 += 1
                c2 = dp[p2] * 2
            if dp[-1] == c3:
                p3 += 1
                c3 = dp[p3] * 3
            if dp[-1] == c5:
                p5 += 1
                c5 = dp[p5] * 5
        return dp[-1]
        