import itertools
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        """
            #prefixsum
        """
        def accumulate2D(A):
            m = len(A)
            n = len(A[0])
            dp = [[0] * (n+1) for _ in range(m+1)] 
            for r,c in itertools.product(range(m), range(n)):
                dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] - dp[r][c] + A[r][c]
            return dp
            
        def rangeSum(dp,r1, c1, r2, c2):
            return dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]
        
        m = len(grid)
        n = len(grid[0])
        state = accumulate2D(grid)
        P = stampHeight * stampWidth
        stamp = [[0]*n for _ in range(m)]
        for r,c in itertools.product(range(stampHeight-1,m),range(stampWidth-1,n)):
            i,j = r-stampHeight+1,c-stampWidth+1
            if rangeSum(state,i,j,r,c) == 0:
                stamp[r][c] += 1
        stampSum = accumulate2D(stamp)
        for r in range(m):
            for c in range(n):
                i = min(r+stampHeight-1,m-1)
                j = min(c+stampWidth-1,n-1)
                if grid[r][c] == 0 and rangeSum(stampSum,r,c,i,j) == 0:
                    return False
        return True