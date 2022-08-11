class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
            #backtrack #dp #bitmask #heap
        """
        n = len(workers)
        m = len(bikes)
        
        # (totaldistance,bike state)
        heap=[(0,0)]
        visited = set()
        while heap:
            cost,state = heapq.heappop(heap)
            i = state.bit_count()
            if i == n:
                return cost
            if state in visited:
                continue
            visited.add(state)
            xw,yw = workers[i]
            for j in range(m):
                if 1 << j & state == 0:
                    xb,yb = bikes[j]
                    heapq.heappush(heap,(cost + abs(xw-xb) + abs(yw-yb),state | 1 << j))
        