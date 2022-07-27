class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
            #bitwise
        """
        res = 0
        for n in nums:
            q, m = divmod(n, original)
            if m == 0 and q == q & -q:
                res |= q
        return (~res & -~res) * original
