class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        """
            #bfs #binarysearch
        """
        def fire():
            queue = deque([])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        queue.append((i,j))
                        grid[i][j] = -1
                
            cnt = -1
            while queue:
                cnt -= 1
                for _ in range(len(queue)):
                    i,j = queue.popleft()
                    for di,dj in (-1,0),(1,0),(0,1),(0,-1):
                        r = i+di
                        c = j+dj
                        if m>r>=0<=c<n and grid[r][c] == 0:
                            queue.append((r,c))
                            grid[r][c] = cnt
        def escape(wait):
            cnt = wait
            queue = deque([(0,0)])
            if grid[0][0] < 0 and cnt >= -grid[0][0]-1:
                return False
            visited = set([(0,0)])
            while queue:
                cnt += 1
                for _ in range(len(queue)):
                    i,j = queue.popleft()
                    
                    if i == m-1 and j == n-1:
                        return True
                    for di,dj in (-1,0),(1,0),(0,1),(0,-1):
                        r = i+di
                        c = j+dj
                        if m>r>=0<=c<n and grid[r][c] <= 0 and (r,c) not in visited:
                            if grid[r][c] < 0:
                                fire = -grid[r][c] - 1
                                if fire == cnt and r == m-1 and c == n-1 or (fire > cnt):
                                    visited.add((r,c))
                                    queue.append((r,c))
                            else:
                                visited.add((r,c))
                                queue.append((r,c))
            return False

        m = len(grid)
        n = len(grid[0])
        fire()
        lo = 0
        hi = m*n
        if escape(hi):
            return 10**9
        if not escape(lo):
            return -1
        while lo < hi:
            mid = (lo+hi)//2 + 1
            if escape(mid):
                lo = mid
            else:
                hi = mid-1
        return lo
