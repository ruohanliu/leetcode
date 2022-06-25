class Solution:
    def countComponents_uf(self, n: int, edges: List[List[int]]) -> int:
        """
            #graph #unionfind
        """
        uf = list(range(n))
        ans = n
        def find(a):
            return a if a == uf[a] else find(uf[a])

        def union(ab):
            nonlocal ans
            a,b = map(find,ab)
            if a != b:
                uf[a] = b
                ans -= 1
                return True
            else:
                return False

        list(map(union,edges))
        return ans

    def countComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v):
            nonlocal adjList,seen
            seen.add(v)
            list(map(dfs,adjList.pop(v,[])))

        adjList = {i:[] for i in range(n)}
        for a,b in edges:
            adjList[a] += b,
            adjList[b] += a,
        
        seen = set()
        ans = 0

        for v in range(n):
            if v not in seen:
                dfs(v)
                ans += 1
        return ans