from typing import List
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
            #bfs #dijkstra #2d
        """
        adjList = defaultdict(list)
        for f,t,p in flights:
            adjList[f].append((t,p))

        dist = [[float("inf")] * n for _ in range(k+2)]
        dist[0][src] = 0
        # (cost,stop,v)
        heap = [(0,0,src)]
        while heap:
            cost,stop,v = heapq.heappop(heap)
            if v == dst:
                return cost
            if stop == k+1 or cost > dist[stop][v]: continue
            for _v,p in adjList[v]:
                _cost = cost + p
                _stop = stop + 1
                if _cost < dist[_stop][_v]:
                    dist[_stop][_v] = _cost
                    heapq.heappush(heap,(_cost,_stop,_v))
        return -1