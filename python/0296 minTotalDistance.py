class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
            #sort #median #twopointer

            O(mn)
        """
        m = len(grid)
        n = len(grid[0])
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    cols.append(j)
        def distance(nums):
            ans = 0
            i = 0
            j = len(nums)-1
            while i<j:
                ans += nums[j]-nums[i]
                i+=1
                j-=1
            return ans

        return distance(cols) + distance(rows)


    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
            O(mnlogmn)
        """
        cols.sort()
        row_median = rows[len(rows)//2]
        col_median = cols[len(rows)//2]
        ans = 0
        for i in range(len(rows)):
            ans += abs(rows[i]-row_median) + abs(cols[i]-col_median)
        return ans

    def minTotalDistance_tle(self, grid: List[List[int]]) -> int:
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i,j,i,j))
                    grid[i][j] = {(i,j):0}
        
        friends = len(queue)
        cnt = 0
        ans = []
        while queue:
            cnt += 1
            for size in range(len(queue)):
                a,b,i,j = queue.popleft()
                for di,dj in directions:
                    r = i + di
                    c = j + dj
                    if 0<=r<m and 0<=c<n:
                        if grid[r][c] == 0:
                            grid[r][c] = {(a,b):cnt}
                            queue.append((a,b,r,c))
                        elif (a,b) not in grid[r][c]:
                            grid[r][c][a,b] = cnt
                            if len(grid[r][c]) == friends:
                                ans.append(sum(grid[r][c].values()))
                            queue.append((a,b,r,c))
        return min(ans)
                        
                
        