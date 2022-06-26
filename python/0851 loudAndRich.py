from collections import defaultdict
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
            #topologicalsort
        """
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        for a,b in richer:
            adjList[a] += b,
            inDegree[b] += 1
        
        queue = [v for v in inDegree if inDegree[v] == 0]
        mostQuietness = {v:quiet[v] for v in range(len(quiet))}
        quietPerson = {quiet[v]:v for v in range(len(quiet))}
        while queue:
            v = queue.pop()
            for _v in adjList[v]:
                mostQuietness[_v]  = min(mostQuietness[v],mostQuietness[_v])
                inDegree[_v] -= 1
                if inDegree[_v] == 0:
                    queue.append(_v)
            del adjList[v]
        return [quietPerson[mostQuietness[v]] for v in range(len(quiet))]

        