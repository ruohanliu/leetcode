class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
            #bfs
            
            find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        queue = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        dist = 0
        while queue:
            dist += 1
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    r = i+di
                    c = j+dj
                    if 0<=r<m and 0<=c<n and grid[r][c] == 0:
                        grid[r][c] = 1
                        queue.append((r,c))
                        ans = dist
                    
        return ans if ans else -1