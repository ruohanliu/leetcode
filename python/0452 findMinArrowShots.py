class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
            #greedy
        """
        points.sort()
        lo = points[-1][0]
        ans = 1
        for a,b in reversed(points):
            if b>=lo:
                continue
            else:
                ans += 1
                lo = a
        return ans                