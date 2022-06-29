from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
            #graph #cyclic #topologicalsort
        """
        n = len(graph)
        adjList = defaultlist(set)
        outDegree = defaultlist(int)
        for i,vertices in enumerate(graph):
            for v in vertices:
                adjList[v].add(i)
                outDegree[i] += 1

        ans = []
        queue = [v for v in range(n) if outDegree[v] == 0]
        while queue:
            v = queue.pop()
            ans.append(v)
            for _v in adjList[v]:
                outDegree[_v] -= 1
                if outDegree[_v] == 0:
                    queue.append(_v)
            del adjList[v]

        return sorted(ans)
        

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
            #graph #cyclic #dfs #important
        """
        def dfs(v,color,graph):
            if color[v] > 0:
                return color[v] == 2

            color[v] = 1

            for _v in graph[v]:
                if color[_v] == 2: continue
                if color[_v] == 1 or not dfs(_v,color,graph): return False

            color[v] = 2
            return True

        n = len(graph)
        color = [0] * n

        ans = []
        for v in range(n):
            if dfs(v,color,graph):
                ans.append(v)
        return ans


