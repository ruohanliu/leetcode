class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
            #dijkstra
        """
        m = len(grid)
        n = len(grid[0])
        dist = [float("inf") * n for _ in range(m)]
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        heap = [(0,0,0)]
        while heap:
            cost,i,j = heapq.heappop(heap)
            if cost > dist[i][j]: continue
            if (i,j) == (m-1,n-1): return cost
            for k,(di,dj) in enumerate(directions):
                r = i+di
                c = j+dj
                if 0<=r<m and 0<=c<n:
                    _cost = cost
                    if grid[i][j]-1 != k:
                        _cost += 1
                    if dist[r][c] > _cost:
                        dist[r][c] = _cost
                        heapq.heappush(heap,(_cost,r,c))
