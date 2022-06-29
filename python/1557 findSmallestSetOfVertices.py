from typing import List
from collections import defaultdict,deque
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
            a directed graph is comprised of acyclic and cyclic components

            traverse all acyclic components first then cyclic components
        """
        adjList = defaultdict(set)
        inDegree = defaultdict(int)
        for a,b in edges:
            adjList[a].add(b)
            inDegree[b]+=1
        
        queue = [v for v in range(n) if inDegree[v] == 0]
        visited = set()
        ans = []
        while queue:
            v = queue.pop()
            visited.add(v)
            ans.append(v)
            stack = [v]
            while stack:
                u = stack.pop()
                for _u in adjList[u]:
                    if _u not in visited:
                        stack.append(_u)
                        visited.add(_u)

        for v in range(n):
            if v not in visited:
                ans.append(v)
                stack = [v]
                while stack:
                    u = stack.pop()
                    for _u in adjList[u]:
                        if _u not in visited:
                            stack.append(_u)
                            visited.add(_u)
        return ans