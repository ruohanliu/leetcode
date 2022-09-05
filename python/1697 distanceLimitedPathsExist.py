class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
            #unionfind #2doptimize
        """
        def find(v):
            _v = v
            while v != uf[v]:
                v = uf[v]
            while _v != v:
                uf[_v],_v = v,uf[_v]
            return v
        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return False
            if size[u] > size[v]:
                size[u]+=size[v]
                uf[v] = u
            else:
                size[v] += size[u]
                uf[u] = v
            return True
        
        uf = list(range(n))
        size = [1] * n

        queries = sorted([(p,q,limit,i) for i,(p,q,limit) in enumerate(queries)],key = lambda x: x[2])
        edgeList.sort(key = lambda x: x[2])

        ans = [False] * len(queries)
        j = -1
        for p,q,limit,i in queries:
            while j+1 < len(edgeList) and edgeList[j+1][2] < limit:
                j+=1
                u,v,_ = edgeList[j]
                union(u,v)
            if find(p) == find(q):
                ans[i] = True
        return ans