class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k,points,key = lambda x:x[0]**2+x[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            #kth #quickselect #algorithm
        """
        return self.quick_select(points, k)

    @cache
    def squared_distance(self,x,y) -> int:
        return x ** 2 + y ** 2
    
    def quick_select(self, points,k):
        lo, hi = 0, len(points) - 1
        pivotIndex = len(points)
        while pivotIndex != k:
            pivotIndex = self.partition(points, lo, hi)
            if pivotIndex < k:
                lo = pivotIndex
            else:
                hi = pivotIndex - 1
        
        return points[:k]
    
    def partition(self, points, lo, hi) -> int:
        pivotPoint = points[random.randrange(lo,hi+1)]
        pivot = self.squared_distance(abs(pivotPoint[0]),abs(pivotPoint[1]))
        while lo < hi:
            if self.squared_distance(abs(points[lo][0]),abs(points[lo][1])) > pivot:
                points[lo], points[hi] = points[hi], points[lo]
                hi -= 1
            else:
                lo += 1
        
        # Ensure the lo pointer is just past the end of
        # the lo range then return it as the new pivotIndex
        if self.squared_distance(abs(points[lo][0]),abs(points[lo][1])) < pivot:
            lo += 1
        return lo
