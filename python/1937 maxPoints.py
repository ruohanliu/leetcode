class Solution:
    def maxPoints_tle(self, points: List[List[int]]) -> int:
        """
            #dp #relation #important

            related 1014 931
        """
        @cache
        def dp(r,c):
            if r == 0:
                return points[0][c]
            ans = float("-inf")
            for c1 in range(n):
                ans = max(ans,dp(r-1,c1) + points[r][c] - abs(c1-c))
            return ans
            
        m = len(points)
        n = len(points[0])
        return max(dp(m-1,c) for c in range(n))

    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        # curr[j] stores the max possible score so far if choosing j in current row
        curr = [0] * n
        prev = curr[:]
        for i in range(m):
            currMax = float("-inf")
            for j in reversed(range(n)):
                currMax = max(currMax-1,prev[j])
                curr[j] = currMax
            currMax = float("-inf")
            for j in range(n):
                currMax = max(currMax-1,prev[j])
                curr[j] = max(curr[j],currMax) + points[i][j]
            prev,curr = curr,prev
        return max(prev)


