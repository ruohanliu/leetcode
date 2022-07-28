class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
            #dp
        """
        @cache
        def dp(i,j,k):
            if not (0<= i <m and 0<=j < n):
                return 1
            if k == 0:
                return 0
            return sum(dp(i+di,j+dj,k-1) for di,dj in ((0,1),(0,-1),(1,0),(-1,0))) % mod
        
        mod = 10**9 + 7
        return dp(startRow,startColumn,maxMove)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        mod = 10**9 + 7
        ans = 0
        for _ in range(maxMove):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ans = (ans + dp[i][j] * sum([i==0,j==0,i==m-1,j==n-1])) % mod
                    temp[i][j] = sum(dp[i+di][j+dj] for di,dj in ((0,1),(0,-1),(1,0),(-1,0)) if 0<=i+di<m and 0<=j+dj < n) % mod
            dp = temp

        return ans