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

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            #precompute
        """
        adjList = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            adjList[a][a] = adjList[b][b] = 1.0
            adjList[a][b] = val
            adjList[b][a] = 1 / val
        for v in adjList:
            for a in adjList[v]:
                for b in adjList[v]:
                    adjList[a][b] = adjList[a][v] * adjList[v][b]
        return [adjList[a].get(b, -1.0) for a, b in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            adjList[a][a] = adjList[b][b] = 1.0
            adjList[a][b] = val
            adjList[b][a] = 1 / val
        
        def dfs(a,b,visited,val):
            if a not in adjList or b not in adjList:
                return float("inf")
            if a == b:
                return val
            visited.add(a)
            ans = None
            for _a in adjList[a]:
                if _a in visited:
                    continue
                res = dfs(_a,b,visited,val*adjList[a][_a])
                if res < float("inf"):
                    return res
            return float("inf")
        return [dfs(a,b,set(),1.0) if dfs(a,b,set(),1.0) < float("inf") else -1.0 for a,b in queries]