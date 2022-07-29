class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
            #dp #multistate
        """
        @cache
        def dp(r,c1,c2):
            if c1 < 0 or c2 < 0 or c1 == n or c2 == n:
                return float("-inf")
            if r == m-1:
                return grid[-1][c1] + grid[-1][c2] if c1 != c2 else grid[-1][c1]

            return (grid[r][c1] + grid[r][c2] if c1 != c2 else grid[r][c1]) + max(\
                dp(r+1,c1-1,c2-1),\
                dp(r+1,c1,c2-1),\
                dp(r+1,c1+1,c2-1),\
                dp(r+1,c1-1,c2),\
                dp(r+1,c1,c2),\
                dp(r+1,c1+1,c2),\
                dp(r+1,c1-1,c2+1),\
                dp(r+1,c1,c2+1),\
                dp(r+1,c1+1,c2+1))


        m = len(grid)
        n = len(grid[0])
        return dp(0,0,n-1)