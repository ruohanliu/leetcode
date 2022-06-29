from typing import List
import heapq
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
            #graph #spanningtree #kruskal #important
        """
        def find(v):
            _v = v
            while uf[v] != v:
                v = uf[v]
            while _v != v:
                _v,uf[_v] = uf[_v],v
            return v

        def union(u,v):
            u = find(u)
            v = find(v)
            if u==v:
                return False
            else:
                if ufs[u] > ufs[v]:
                    uf[v] = u
                    ufs[u] += ufs[v]
                else:
                    uf[u] = v
                    ufs[v] += ufs[u]
                return True
        
        uf = [i for i in range(n+1)]
        ufs = [0] * (n+1)
        edges = [(w,a,b) for a,b,w in connections]
        heapq.heapify(edges)
        cnt = 0
        ans = 0
        while cnt < n-1 and edges:
            w,a,b = heapq.heappop(edges)
            if union(a,b):
                cnt += 1
                ans += w
        return ans if cnt == n-1 else -1