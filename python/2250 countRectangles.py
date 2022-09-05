class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        """
            #fenwicktree #sortedlist #important #2Doptimize #furtherstudy

            https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/discuss/1984225/BIT
        """
        from sortedcontainers import SortedList
        rectangles.sort()
        n = len(rectangles)
        m = len(points)
        ans = [0] * m
        points = sorted([(x,y,i) for i,(x,y) in enumerate(points)],reverse=True)
        sl = SortedList()
        j = n-1
        for x,y,p in points:
            # all the rect to the right have sufficient w
            i = bisect.bisect_left(rectangles,[x,1])
            while i<=j:
                sl.add(rectangles[j][1])
                j-=1
            ans[p] = len(sl) - sl.bisect_left(y)
        return ans


