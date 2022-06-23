class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
            #rectangle #overlap

            Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
        """
        areaA = (ax2-ax1) * (ay2-ay1)
        areaB = (bx2-bx1) * (by2-by1)
        
        if max(ax1,ax2) <= min(bx1,bx2) or max(bx1,bx2) <= min(ax1,ax2) or max(ay1,ay2) <= min(by1,by2) or max(by1,by2) <= min(ay1,ay2):
            areaC = 0
        else:
            xs = sorted([ax1,ax2,bx1,bx2])
            ys = sorted([ay1,ay2,by1,by2])
            areaC = (xs[2]-xs[1]) * (ys[2]-ys[1])
            
        return areaA+areaB-areaC