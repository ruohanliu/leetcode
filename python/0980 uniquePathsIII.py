class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
            #dp #bitmask #backtrack
        """
        @cache
        def dp(state,pos):
            i,j  = pos
            if pos == start:
                return 1 if state == (1<<(m*n)) - 1 else 0
            ans = 0
            for di,dj in directions:
                r = i+di
                c = j+dj
                if 0<=r<m and 0<=c<n and state & 1 << (r * n + c) == 0:
                    ans += dp(state | 1 << (r * n + c),(r,c))
            return ans

        m = len(grid)
        n = len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        start = end = None
        state = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                    pos = i * n + j
                    state += 1 << pos
                elif grid[i][j] == -1:
                    pos = i * n + j
                    state += 1 << pos

        return dp(state,end)

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x, y, empty):
            nonlocal ans
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
            if grid[x][y] == 2:
                ans += empty == 0
                return
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0

        ans = 0
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1
        dfs(x, y, empty)
        return ans