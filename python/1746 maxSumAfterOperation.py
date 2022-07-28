class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        """
            #kadane
        """
        square = noSquare = 0
        ans = float("-inf")
        for n in nums:
            noSquare,square = max(n,noSquare+n),max(n**2,noSquare+n**2,square+n)
            ans = max(ans,square)
        return ans