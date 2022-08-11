from typing import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
            #sort #heap #hard #important
            related: 1996 numberOfWeakCharacters 857 minCostToHireWorkers
            
            it is a two-dimension optimization problem. fix one dimension, enumerate on the other.
            iterate from the greatest efficiency to allow one pass of candidates. does not need to sort on speed because heap is used.

            If curr_speed > popped speed, cur_speed should be in the heap.
            If curr_speed < popped_speed, it means that it will be the new minimum and will be popped during next iteration anyway.
        """
        import heapq

        mod = 10**9 + 7
        candidates = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)

        ans = 0
        heap = []
        speed_sum = 0
        for eff,spe in candidates:
            heapq.heappush(heap,spe)
            speed_sum += spe
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            
            ans = max(ans,eff*speed_sum)
        return ans % mod