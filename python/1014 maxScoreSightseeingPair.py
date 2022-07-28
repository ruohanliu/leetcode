class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
            #kadane
        """
        ans = float("-inf")
        curr = values[0]
        for i in range(1,len(values)):
            curr -= 1
            ans = max(ans,curr + values[i])
            curr = max(curr,values[i])
        return ans