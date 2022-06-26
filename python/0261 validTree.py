from typing import List
class Solution:
    def validTree_uf_simple(self, n: int, edges: List[List[int]]) -> bool:
        """
            #unionfind #graph #treegraph #undirected #important

            Return true if the edges of the given graph make up a valid tree, and false otherwise.

            O(EV)
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

    def validTree_uf_pathcompression(self, n: int, edges: List[List[int]]) -> bool:
        """
            #pathcompression
            O(Elog*V)
        """
        if len(edges) != n - 1:
            return False
        
        uf = list(range(n))
        rank = [1] * n

        def find(a):
            """
                or the following

                _a = a
                while a != uf[a]:
                    a = uf[a]
                while _a != a:
                    _a,uf[_a] = uf[_a],a
                return a 
            """
            while a != uf[a]:
                uf[a] == uf[uf[a]]
                a = uf[a]
            return a 

        def union(ab):
            a,b = map(find,ab)
            if a == b:
                return False
            if rank[a] > rank[b]:
                rank[a] += rank[b]
                uf[b] = a
            else:
                rank[b] += rank[a]
                uf[a] = b
            return True
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