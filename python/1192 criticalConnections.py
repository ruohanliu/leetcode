class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
            #dfs #cycle #important #rank

            an edge is critical edge iff it is not part of a cycle
        """

        def dfs(v,d):
            nonlocal adjList,visited,edges
            if visited[v] >= 0:
                return visited[v]

            visited[v] = d
            minRank = n
            for _v in adjList[v]:
                # v coming from _v
                if visited[_v] == d-1:
                    continue
                rank = dfs(_v,d+1)
                # v_v is an edge of a cylce
                if rank <= d:
                    edges.discard(tuple(sorted([v,_v])))
                minRank = min(minRank,rank)
            
            return minRank

        adjList = defaultdict(list)
        for a,b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = [-2] * n
        edges = set(map(tuple,map(sorted,connections)))
        dfs(0,0)

        return edges