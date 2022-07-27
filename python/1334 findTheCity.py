from typing import List
from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
            #graph #dijkstra
        """
        adjList = defaultdict(set)
        for a,b,w in edges:
            adjList[a].add((b,w))
            adjList[b].add((a,w))

        ans = (float("inf"),float("inf"))
        for v in range(n):
            heap = [(0,v)]
            seen = set()
            while heap:
                cost,u = heapq.heappop(heap)
                if u in seen:
                    continue
                seen.add(u)
                for _u,w in adjList[u]:
                    if _u not in seen and cost+w <= distanceThreshold:
                        heapq.heappush(heap,(cost + w,_u))

            ans  = min(ans,(len(seen)-1,-v))
        return -ans[1]

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
            #Floyd–Warshall #important

            order of ijk matters

            finding shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles)
        """
        dist = [[float("inf")] * n for _ in range(n)]
        for a,b,w in edges:
            dist[a][b] = w
            dist[b][a] = w

        for i in range(n):
            dist[i][i] = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[j][k] = min(dist[j][k],dist[i][j] + dist[i][k])

        cnt = float("inf")
        for i in range(n):
            new = sum(dist[i][j] <= distanceThreshold for j in range(n))
            if new <= cnt:
                v = i
                cnt = new
        return v