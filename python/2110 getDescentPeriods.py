from typign import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
            # of subarrays = (n+1)n/2
        """
        i = 0
        j = 0
        ans = 0
        while i < len(prices):
            if j+1 < len(prices) and prices[j] == prices[j+1] + 1:
                j += 1
                continue
            # found a period
            else:
                n = j-i + 1
                ans += (n + 1) * n / 2
                i = j+1
                j += 1

        return ans

    def getDescentPeriods(self, prices: List[int]) -> int:
        """
           simpler implementation
        """
        ans = 0 
        for i, x in enumerate(prices): 
            if i == 0 or prices[i-1] != x + 1: cnt = 0
            cnt += 1
            ans += cnt 
        return ans 

