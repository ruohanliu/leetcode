class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
            #bfs
        """
        # label each island with unique id
        # record size of each island
        # a bridge could collect up to 4 island
        
        def bfs(i,j,cnt):
            queue = deque([(i,j)])
            grid[i][j] = cnt
            ans = 0
            while queue:
                i,j = queue.popleft()
                ans += 1
                for di,dj in directions:
                    r = i + di
                    c = j + dj
                    if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                        grid[r][c] = cnt
                        queue.append((r,c))
            return ans
            
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        size = {}
        m = len(grid)
        n = len(grid[0])
        cnt = 1
        ans = 0
        hasWater = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    size[cnt] = bfs(i,j,cnt)
                    ans = max(ans,size[cnt])
                elif grid[i][j] == 0:
                    hasWater = 1
                    
        ans += hasWater
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    candidate = 1
                    seen = set()
                    for di,dj in directions:
                        r = i + di
                        c = j + dj
                        if 0<=r<m and 0<=c<n and grid[r][c]>1 and grid[r][c] not in seen:
                            seen.add(grid[r][c])
                            candidate += size[grid[r][c]]
                    ans = max(ans,candidate)
        return ans
    
        