class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
            #heap #sort
            related 1383 maxPerformance            
            sort by wage/quality ratio. iterate from the smallest ratio, choose the k least quality workers
        """
        heap = []
        ans = float("inf")
        total_quality = 0
        for ratio,q,w in sorted((w / q,q,w) for q,w in zip(quality,wage)):
            heapq.heappush(heap,-q)
            total_quality += q
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans,ratio * total_quality)
        return ans
            