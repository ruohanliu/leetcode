class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
            #kruskal #virtualvertext
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
        
        ds = [i for i in range(n+1)]
        size = [1] * (n+1)
        edges = [(w,a,b) for a,b,w in pipes] + [(w,0,i+1) for i,w in enumerate(wells)]
        heapq.heapify(edges)
        cnt = 0
        ans = 0
        while cnt < n:
            w,a,b = heapq.heappop(edges)
            if union(a,b):
                cnt += 1
                ans += w
        return ans


    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
            #prim #important
        """
        adjList = defaultdict(list)
        for i, cost in enumerate(wells):
            adjList[0].append((cost, i+1))
        for v, u, cost in pipes:
            adjList[v].append((cost, u))
            adjList[u].append((cost, v))

        visited = set()
        heap = [(0,0)]
        ans = 0
        while True:
            cost,v = heapq.heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            ans += cost
            if len(visited) == n+1:
                return ans
            for _cost,_v in adjList[v]:
                if _v not in visited:
                    heapq.heappush(heap,(_cost,_v))