class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
            #unionfind #2d

            do not use recursive find(), may result in stack overflow
        """
        def find(r,c):
            if grid[r][c] != (r,c):
                grid[r][c] = find(*grid[r][c])
            return grid[r][c]
        
        def union(c1,c2):
            c1 = find(*c1)
            c2 = find(*c2)
            if c1 == c2:
                return False
            else:
                r1,c1 = c1
                r2,c2 = c2
                if size[r1][c1] > size[r2][c2]:
                    size[r1][c1]+=size[r2][c2]
                    grid[r2][c2] = (r1,c1)
                else:
                    size[r2][c2]+=size[r1][c1]
                    grid[r1][c1] = (r2,c2)
                return True
        def add(pos):
            nonlocal ans,cnt
            r,c = pos
            if grid[r][c] == 0:
                grid[r][c] = (r,c)
                cnt +=1
                for dr,dc in d:
                    i = r+dr
                    j = c+dc
                    if 0<=i<m and 0<=j<n and grid[i][j]:
                        if union((i,j),(r,c)):
                            cnt -= 1
            ans+=cnt,

        grid = [[0] * n for _ in range(m)]
        size = [[1] * n for _ in range(m)]
        d = ((-1,0),(1,0),(0,-1),(0,1))
        ans = []
        cnt = 0
        list(map(add,positions))
        return ans