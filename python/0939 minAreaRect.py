from typing import List
from collections import defaultdict
class Solution:
    def minAreaRect_tle(self, points: List[List[int]]) -> int:
        """
            #coordinate #rectangle
        """
        n = len(points)        
        rec = []
        res = float("inf")
        points.sort()
        pointSet = set((x,y) for x,y in points)
        
        i = 0
        while True:
            if i < n:
                if not rec:
                    rec.append(i)
                elif len(rec) == 1:
                    if points[i][0] > points[rec[0]][0] or (points[i][1] - points[rec[0]][1]) > res:
                        i = rec.pop()
                    else:
                        rec.append(i)
                elif len(rec) == 2:
                    if (points[i][0] - points[rec[0]][0]) * (points[rec[1]][1] - points[rec[0]][1]) > res:
                        i = rec.pop()
                    elif points[i][1] == points[rec[0]][1]:
                        if (points[i][0],points[rec[1]][1]) in pointSet:
                            res = min(res,(points[rec[1]][1] - points[rec[0]][1]) * (points[i][0] - points[rec[0]][0]))
                i+=1
            else:
                if not rec:
                    break
                i = rec.pop() + 1

        return res if res < float("inf") else 0

    def minAreaRect_tle(self, points: List[List[int]]) -> int:
        """
            #vectorization
        """
        xMap = defaultdict(set)
        for p in points:
            xMap[p[0]].add(p[1])
        ans = float("inf")

        xs = [x for x in xMap if len(xMap[x])>=2]
        n = len(xs)
        for i in range(n-1):
            for j in range(i+1, n):
                dY = float("inf")
                last = float("-inf")
                for y in sorted(xMap[xs[i]] & xMap[xs[j]]):
                    dY = min(dY,y-last)
                    last = y
                ans = min(ans,abs(xs[i] - xs[j]) * dY)
        return ans if ans != float("inf") else 0
