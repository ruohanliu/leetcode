class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
            #math #digit
        """
        limit = str(n)
        n = len(limit)
        m = len(digits)
        # result for numbers with fewer digits than n
        ans = sum(m ** i for i in range(1, n))
        i = 0
        while i < n:
            ans += sum(c < limit[i] for c in digits) * (m ** (n - i - 1))
            # if there is c == limit[i], then consider limit[i+1]; otherwise no need to consider further
            if limit[i] not in digits: break
            i += 1
        # if while loop didnt break, every digit of n is in digits, add 1 last number which is exactly n
        return ans + (i == n)