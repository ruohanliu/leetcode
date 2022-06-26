from typing import List
from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
            #graph #tree #diameter
                1. find one endpoint of the longest path using bfs/dfs
                2. use dfs to find another endpoint
        """

        adjList = {v:set() for v in range(n)}
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        def dfs(v,d):
            nonlocal maxLen,u
            if perm[v]:
                return
            perm[v] = True
            d+=1
            if d > maxLen:
                maxLen = d
                u = v

            for _v in adjList[v]:
                dfs(_v,d)
            
        n = len(edges) + 1
        u = None

        maxLen = 0
        perm = [False] * n
        dfs(0,0)

        perm = [False] * n
        dfs(u,0)

        return maxLen-1

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
            #topologicalsort
            edge case: edges is empty
        """
        if not edges:
            return 0
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        ans = 0
        leaves = [v for v in adjList.keys() if len(adjList[v]) == 1]
        while len(adjList)>1:
            ans += 2
            nextLeaves = []
            while leaves:
                leaf = leaves.pop()
                for parent in adjList[leaf]:
                    adjList[parent].discard(leaf)
                    if len(adjList[parent]) == 1:
                        nextLeaves.append(parent)
                del adjList[leaf]
            leaves = nextLeaves

        return ans if adjList else ans-1