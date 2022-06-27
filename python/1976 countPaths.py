from typing import List
from collections import defaultdict
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
            #graph #dijkstra
        """
        mod = 10**9 +7
        adjList = defaultdict(set)
        for a,b,w in roads:
            adjList[a].add((b,w))
            adjList[b].add((a,w))

        heap = [(0,0)]
        dist = [float("inf")] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        while heap:
            cost,u = heapq.heappop(heap)
            if dist[u] < cost:
                continue
            for _u,w in adjList[u]:
                adjList[_u].discard(u)
                if cost + w < dist[_u]:
                    dist[_u] = cost + w
                    ways[_u] = ways[u]
                    heapq.heappush(heap,(cost + w,_u))
                elif cost + w == dist[_u]:
                    ways[_u] = (ways[_u] + ways[u]) % mod
            del adjList[u]
            
        return ways[n-1]