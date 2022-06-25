from typing import List
class Solution:
    def validTree_uf(self, n: int, edges: List[List[int]]) -> bool:
        """
            #unionfind #graph #treegraph #undirected #important

            Return true if the edges of the given graph make up a valid tree, and false otherwise.
        """
        if len(edges) != n - 1:
            return False
        
        uf = list(range(n))
        def find(a):
            return a if uf[a] == a else find(uf[a])
        def union(ab):
            a,b = map(find,ab)
            uf[a] = b
            return a != b
        return all(union(edge) for edge in edges)
            

    def validTree_dfs(self, n, edges):
        """
            #graph #traverse
            
            adjList must include all vertices
            short-hand for append item to list:  `list += ele,`

            adjMatrix is usualy used when the number of edges are significantly more than number of vertices
        """
        if len(edges) != n - 1:
            return False
        
        adjList = {x:[] for x in range(n)}
        for a, b in edges:
            adjList[a] += b,
            adjList[b] += a,

        def visit(v):
            list(map(visit, adjList.pop(v, [])))
        visit(0)
        return not adjList

    def validTree_dfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a] += b,
            adjList[b] += a,
            
        seen = set()
        def dfs(v):
            seen.add(v)
            for _v in adjList[v]:
                if _v in seen:
                    continue
                dfs(_v)
        dfs(0)
            
        return n == len(seen)