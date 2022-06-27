from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
            #graph #dfs #DAG

            no need for checking visited node since it is DAG

            Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
        """
        def dfs(v,path):
            nonlocal ans,n,graph
            path.append(v)
            if v == n-1:
                ans.append(path.copy())
            for _v in graph[v]:
                dfs(_v,path)
            path.pop()
            
        n = len(graph)
        ans = []
        dfs(0,[])
        return ans