class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
            #bfs with obstacle
        """
        m = len(grid)
        n = len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))    
        cnt = 0
        dist = [[0] * n for _ in range(m)]
        for i,j in product(range(m),range(n)):
            if grid[i][j] == 1:
                queue = deque([(i,j)])
                valid = False
                curr = 0
                while queue:
                    for _ in range(len(queue)):
                        x,y = queue.popleft()
                        dist[x][y] += curr
                        for dx,dy in directions:
                            r,c = x+dx,y+dy
                            if m>r>=0<=c<n and grid[r][c] == cnt:
                                queue.append((r,c))
                                grid[r][c] -= 1
                                valid = True
                    curr += 1
                cnt -= 1
                if not valid:
                    return -1
        
        ans = float("inf")
        for i,j in product(range(m),range(n)):
            if grid[i][j] == cnt:
                ans = min(ans,dist[i][j])
        return ans