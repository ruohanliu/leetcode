class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        """
            #graph #dfs
        """
        def dfs(v,curr,target):
            nonlocal visited
            if v == target:
                return curr
            visited.add(v)
            for _v,val in adjList[v]:
                if _v in visited:
                    continue
                res = dfs(_v,curr*val,target)
                if res:
                    return res
            return None

        adjList = defaultdict(list)
        for (a,b),val in zip(equations,values):
            visited=set()
            res = dfs(a,1.0,b)
            if res and abs(res - val) >= 1e-5:
                return True
            adjList[a].append((b,val))
            adjList[b].append((a,1.0/val))
        return False
