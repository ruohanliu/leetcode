class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
            #geometricmedian #proximation #centroid
        """
        fn = lambda x,y: sum(math.sqrt((x-i)**2+(y-j)**2) for i,j in positions)
        n = len(positions)
        x = 0
        y = 0
        for i,j in positions:
            x += i
            y += j
        x /= n
        y /= n
        delta = 100
        ans = fn(x,y)
        while delta > 1e-6:
            zoom = True
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                candidate = fn(x+dx*delta,y+dy*delta)
                if candidate < ans:
                    x += dx*delta
                    y += dy*delta
                    zoom = False
                    ans = candidate
                    break
            if zoom:
                delta /= 2
        return ans