class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            #graph #dfs
        """
        def dfs(root,v,currVal):
            nonlocal adjList,expandedEquations,visited
            visited.add(v)
            for _v,val in adjList[v]:
                if _v not in visited:
                    nextVal = currVal * val
                    expandedEquations[(root,_v)] = nextVal
                    dfs(root,_v,nextVal)

        expandedEquations = {}
        adjList = defaultdict(list)
        for (a,b),val in zip(equations,values):
            adjList[a].append((b,val))
            adjList[b].append((a,1/val))

        for v in adjList:
            visited = set()
            dfs(v,v,1)

        ans = []
        vertices = set(adjList.keys())
        for x,y in queries:
            if x not in vertices or y not in vertices:
                ans.append(-1.0)
            elif x==y:
                ans.append(1.0)
            else:
                ans.append(expandedEquations[(x,y)] if (x,y) in expandedEquations else -1.0)
        return ans