class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            #prim
        """
        n = len(points)
        remaining = set(i for i in range(1,n))
        heap = []
        x1,y1 = points[0]
        for i in range(1,n):
            heapq.heappush(heap,(abs(x1-points[i][0])+abs(y1-points[i][1]),i))
        point = 0
        ans = 0
        while remaining:
            dist,j = heapq.heappop(heap)
            if j in remaining:
                ans += dist
                x1,y1 = points[j]
                remaining.remove(j)
                for i in remaining:
                    heapq.heappush(heap,(abs(x1-points[i][0])+abs(y1-points[i][1]),i))
        return ans

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            #kruskal
        """
        def find(v):
            _v = v
            while ds[v] != v:
                v = ds[v]
            while _v != v:
                _v,ds[_v] = ds[_v],v
            return v

        def union(u,v):
            u = find(u)
            v = find(v)
            if u==v:
                return False
            else:
                if size[u] > size[v]:
                    ds[v] = u
                    size[u] += size[v]
                else:
                    ds[u] = v
                    size[v] += size[u]
                return True
        
        n = len(points)
        ds = [i for i in range(n)]
        size = [1] * n
        edges = [(abs(x1-x2)+abs(y1-y2),i,j) for i,(x1,y1) in enumerate(points) for j,(x2,y2) in enumerate(points) if j>i]
        heapq.heapify(edges)
        ans = 0
        cnt = 0
        while cnt < n-1:
            w,i,j = heapq.heappop(edges)
            if union(i,j):
                cnt += 1
                ans += w
        return ans