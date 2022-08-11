class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
            #frozenset
        """
        def bfs(i,j):
            queue = [(i,j)]
            grid[i][j] = -1
            si,sj = i,j
            ans = []
            while queue:
                i,j = queue.pop()
                ans += (i-si,j-sj),
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if r>=0 and r<m and c >=0 and c<n and grid[r][c] == 1:
                        grid[r][c] = -1
                        queue.append((r,c))
            t = frozenset(ans)
            if t not in islandKey:
                islandKey.add(t)
                return 1
            else:
                return 0
        
        d = ((-1,0),(1,0),(0,-1),(0,1))
        
        m = len(grid)
        n = len(grid[0])
        islandKey = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += bfs(i,j)
                    
        return ans