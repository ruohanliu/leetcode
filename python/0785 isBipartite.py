class Solution:
    def isBipartite(self, adjList: List[List[int]]) -> bool:
        """
            #graph #bipartition
        """
        n = len(adjList)
        color = [0] * n
        for v in range(n):
            if not color[v] and adjList[v]:
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
        return True
