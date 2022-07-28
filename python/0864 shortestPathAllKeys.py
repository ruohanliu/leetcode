class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
            #bfs #bitwise
        """
        m = len(grid)
        n = len(grid[0])
        d = ((0,1),(0,-1),(1,0),(-1,0))

        queue = deque([])
        totalLocks = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    queue.append((i,j,0))
                elif grid[i][j].isupper():
                    totalLocks |= 1<<(ord(grid[i][j])-65)

        dist = [[[float("inf")]*(totalLocks+1) for _ in range(n)] for _ in range(m)]
        steps = 0
        while queue:
            size = len(queue)
            steps += 1
            for _ in range(size):
                i,j,status = queue.popleft()
                if steps-1 > dist[i][j][status]: continue
                if status == totalLocks:
                    return steps-1
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if 0<=r<m and 0<=c<n and grid[r][c] != "#":
                        _status = status
                        if grid[r][c].islower():
                            _status |= 1<<(ord(grid[r][c])-97)
                        if not (grid[r][c].isupper() and status & 1<<(ord(grid[r][c])-65) == 0) and steps < dist[r][c][_status]:
                            dist[r][c][_status] = steps
                            queue.append((r,c,_status))
        return -1
