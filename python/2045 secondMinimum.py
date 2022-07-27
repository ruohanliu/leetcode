from typing import List
from collections import defaultdict
import heapq
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        """
            #dijkastra #important

            because edge weight is fixed, it would be enough to just select the first 2 visits for each vertex to ensure they are the two min cost.
            two path could still arrive at a vertex at the same time
        """
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        dist = [0] * (n+1)
        dist[1] = 0
        visited = [0] * (n+1)

        heap = [(0,1)]
        while heap:
            cost,v = heapq.heappop(heap)
            for _v in adjList[v]:
                if cost//change % 2 == 0:
                    arrivalTime = cost+time
                    if visited[_v] == 0:
                        dist[_v] = arrivalTime
                        visited[_v] += 1
                        heapq.heappush(heap,(arrivalTime,_v))
                    elif visited[_v] == 1 and arrivalTime != dist[_v]:
                        visited[_v] += 1
                        if _v == n: return arrivalTime
                        heapq.heappush(heap,(arrivalTime,_v))
                else:
                    arrivalTime = change - (cost % change) + cost + time
                    if visited[_v] == 0:
                        dist[_v] = arrivalTime
                        visited[_v] += 1
                        heapq.heappush(heap,(arrivalTime,_v))
                    elif visited[_v] == 1 and arrivalTime != dist[_v]:
                        visited[_v] += 1
                        if _v == n: return arrivalTime
                        heapq.heappush(heap,(arrivalTime,_v))