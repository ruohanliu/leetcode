class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        """
            #digit #dp #math

            related 233
        """
        # return result between [1,N-1]
        def count(N):
            if N == 0: return 0
            if d == 0 and N <= 10: return 0
            ans = 0
            if N % 10 > d: ans += 1
            if N // 10 > 0: ans += str(N // 10).count(str(d)) * (N % 10)
            ans += N // 10 if d else N // 10 - 1
            ans += count(N // 10) * 10
            return ans
        return count(high + 1) - count(low)