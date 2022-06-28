class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
            #bfs
            
            find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1
        """
        def bfs_land(i,j,landCells):
            queue = [(i,j)]
            grid[i][j] = -1
            while queue:
                i,j = queue.pop()
                landCells.append((i,j))
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if r>=0 and r<m and c >=0 and c<n and grid[r][c] == 1:
                        grid[r][c] = -1
                        queue.append((r,c))
        
        d = ((-1,0),(1,0),(0,-1),(0,1))
        
        m = len(grid)
        n = len(grid[0])
        
        landCells = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs_land(i,j,landCells)
        dist = 0
        while landCells:
            nextCells = []
            while landCells:
                i,j = landCells.pop()
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if r>=0 and r<m and c >=0 and c<n and grid[r][c] == 0:
                        grid[r][c]=-1
                        nextCells.append((r,c))
            if nextCells:
                dist += 1
            landCells = nextCells
                    
        return dist if dist else -1