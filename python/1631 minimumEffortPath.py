class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
            #dijkstra #2d #dp
        """
        m = len(heights)
        n = len(heights[0])
        
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = 0
        
        heap = [(0,0,0)]
        directions = ((0,-1),(0,1),(1,0),(-1,0))
        while heap:
            cost,i,j = heapq.heappop(heap)
            if (i,j) == (m-1,n-1):
                return cost
            if cost > dp[i][j]: continue
            for dx,dy in directions:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and max(cost,abs(heights[x][y] - heights[i][j])) < dp[x][y]:
                    dp[x][y] = max(cost,abs(heights[x][y] - heights[i][j]))
                    heapq.heappush(heap,(dp[x][y],x,y))
