from typing import List
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
            #graph #bipartition #important

            a bipartition graph cannot have odd cycle
        """
        def dfs(v,c):
            nonlocal adjList,color
            if color[v]:
                return c == color[v]

            color[v] = c
            res = True
            for _v in list(adjList[v]):
                adjList[_v].discard(v)
                res &= dfs(_v,c*-1)
            del adjList[v]
            
            return res

        adjList = defaultdict(set)
        for a,b in dislikes:
            adjList[a].add(b)
            adjList[b].add(a)

        color = [0] * (n+1)
        return all(dfs(v,1) for v in range(1,n+1) if color[v] == 0)

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for a,b in dislikes:
            adjList[a].add(b)
            adjList[b].add(a)
        color = [0] * (n+1)

        for v in range(1,n+1):
            if not color[v]:
                stack = [v]
                color[v] = 1
                while stack:
                    u = stack.pop()
                    for _u in adjList[u]:
                        if not color[_u]:
                            color[_u] = color[u]*-1
                            stack.append(_u)
                        elif color[_u] == color[u]:
                            return False
                    del adjList[u]
        return True


        