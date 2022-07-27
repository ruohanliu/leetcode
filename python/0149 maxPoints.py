from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
            #math
        """
        def gcd(a,b):
            while a:
                a,b = b%a,a
            return b

        def slope(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            if x1 == x2:
                return (x1,None)
            else:
                g = gcd(y2-y1,x2-x1)
                return ((y2-y1)//g,(x2-x1)//g)

        n = len(points)
        slopeDict = {}
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                a = slope(points[i],points[j])
                if a not in slopeDict:
                    slopeDict[a] = defaultdict(int)
                if not a[1]:
                    b = None
                else:
                    b = points[i][1] - points[i][0]*a[0]/a[1]
                slopeDict[a][b]+=1
                ans = max(ans,slopeDict[a][b])

        return math.isqrt(2*ans)+1
