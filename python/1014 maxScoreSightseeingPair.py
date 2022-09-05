class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
            #kadane #important
        """
        ans = float("-inf")
        curr = 0
        for x in values:
            ans = max(ans,curr + x)
            curr = max(curr,x) - 1
        return ans