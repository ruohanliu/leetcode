class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
            #dijkstra

            find a route with min max number
        """

        m = len(grid)
        n = len(grid[0])
        state = [[float("inf")] * n for _ in range(m)]
        heap = [(grid[0][0],0,0)]
        while heap:
            curr,i,j = heapq.heappop(heap)
            if state[i][j] < curr:
                continue
            if (i,j) == (m-1,n-1):
                return curr
            for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                _i = i+di
                _j = j+dj
                if 0<=_i <m and 0<=_j<n:
                    candidate = max(curr,grid[_i][_j])
                    if candidate < state[_i][_j]:
                        state[_i][_j] = candidate
                        heapq.heappush(heap,(candidate,_i,_j))
        