class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
            dfs/bfs record visited status early when adding to stack/queue.
        
        """
        def bfs(i,j):
            surrounded = True
            queue = [(i,j)]
            grid[i][j]=-1
            while queue:
                i,j = queue.pop()
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if not (r>=0 and r<m and c >=0 and c<n):
                        surrounded = False
                    else:
                        if grid[r][c] == 0:
                            grid[r][c] = -1
                            queue.append((r,c))
            return surrounded
        
        d = ((-1,0),(1,0),(0,-1),(0,1))
        
        m = len(grid)
        n = len(grid[0])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += bfs(i,j)
        return ans