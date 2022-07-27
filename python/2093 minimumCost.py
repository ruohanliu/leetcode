from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        """
            #graph #dijkstra #2d #important
        """
        adjList = defaultdict(set)
        for a,b,w in highways:
            adjList[a].add((b,w))
            adjList[b].add((a,w))

        dist = [[float("inf")] * n for _ in range(discounts+1)]

        dist[discounts][0] = 0
        heap = [(0,0,discounts)]
        while heap:
            cost,v,discount = heapq.heappop(heap)
            if v == n-1:
                return cost
            if dist[discount][v] < cost: continue
            for _v,w in adjList[v]:
                if dist[discount][_v] > cost + w:
                    dist[discount][_v] = cost + w
                    heapq.heappush(heap,(cost+w,_v,discount))
                if discount and dist[discount-1][_v] > cost + w//2:
                    dist[discount-1][_v] = cost + w//2
                    heapq.heappush(heap,(cost+w//2,_v,discount - 1))

        return -1