from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        """
            #dijkstra
        """

        n = len(patience)
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        dist = [float("inf")] * n

        heap = [(0,0)]
        while heap:
            cost, v = heapq.heappop(heap)
            if cost > dist[v]: continue

            for _v in adjList[v]:
                if cost + 1 < dist[_v]:
                    dist[_v] = cost+1
                    heapq.heappush(heap,(cost+1,_v))
        res = 0
        for v in range(1,n):
            cost = dist[v] * 2
            res = max(res,(cost // patience[v] - (cost % patience[v] == 0))*patience[v]+cost)
        return res+1