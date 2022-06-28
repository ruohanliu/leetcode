from collections import defaultdict
from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            #graph #dijkstra
        """
        dist = [float("inf")] * (1+n)
        dist[k] = 0
        heap = [(0,k)]
        adjList = defaultdict(set)
        for a,b,w in times:
            adjList[a].add((b,w))

        cnt = 0
        while heap:
            cost,v = heapq.heappop(heap)
            if dist[v] < cost: continue
            cnt += 1
            if cnt == n:
                return cost
            for _v,w in adjList[v]:
                if cost+w < dist[_v]:
                    dist[_v] = cost+w
                    heapq.heappush(heap,(cost+w,_v))
            del adjList[v]
            
        return -1