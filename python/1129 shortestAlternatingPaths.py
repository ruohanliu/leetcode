import heapq
from collections import defaultdict
from typing import List
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
            #graph #dijkastra
        """
        heap = [(0,0,1),(0,0,2)]
        distRed = [float("inf")] * n
        distRed[0] = 0
        distBlue = [float("inf")] * n
        distBlue[0] = 0
        adjRed = defaultdict(set)
        adjBlue = defaultdict(set)
        for a,b in redEdges:
            adjRed[a].add(b)
        for a,b in blueEdges:
            adjBlue[a].add(b)
        while heap:
            cost,v,color = heapq.heappop(heap)
            # red
            if color == 1:
                # continue
                if distRed[v] < cost: continue
                for _v in adjBlue[v]:
                    if distBlue[_v] > cost + 1:
                        distBlue[_v] = cost + 1
                        heapq.heappush(heap,(cost + 1,_v,2))
                del adjBlue[v]
            # blue
            else:
                # continue
                if distBlue[v] < cost: continue
                for _v in adjRed[v]:
                    if distRed[_v] > cost + 1:
                        distRed[_v] = cost + 1
                        heapq.heappush(heap,(cost + 1,_v,1))
                del adjRed[v]
        return [min(distRed[i],distBlue[i]) if min(distRed[i],distBlue[i]) < float("inf") else -1 for i in range(n)]