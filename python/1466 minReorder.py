from typing import List
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
            #graph #dfs #important
            dict.popitem()
        """

        def dfs(v):
            color[v] = 2
            del unreachable[v]
            for _v in adjList[v]:
                if color[_v] == 0:
                    color[_v] = 1
                    unreachable[_v] = v

            for _v in adjListReversed[v]:
                dfs(_v)
        
        adjList = defaultdict(set)
        adjListReversed = defaultdict(set)
        for a,b in connections:
            adjList[a].add(b)
            adjListReversed[b].add(a)
        # 0 = unvisited
        # 1 = adjacent but unreachable
        # 2 = reachable
        color = [0] * n
        unreachable = {}
        ans = 0
        dfs(0)
        while unreachable:
            u,v = unreachable.popitem()
            adjList[v].discard(u)
            adjList[u].add(v)
            adjListReversed[u].discard(v)
            adjListReversed[v].add(u)
            ans += 1
            dfs(u)
        
        return ans