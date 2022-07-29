class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
            #dp #multistate
        """
        @cache
        def dp(r1,c1,r2):
            c2 = r1+c1-r2
            if n in (r1,c1,r2,c2) or -1 in (grid[r1][c1],grid[r2][c2]):
                return float("-inf")
            if r1 == c1 == n-1:
                return grid[r1][c1]
            return grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0) + max(dp(r1,c1+1,r2+1),dp(r1+1,c1,r2+1),dp(r1,c1+1,r2),dp(r1+1,c1,r2))
        
        n = len(grid)
        return max(0,dp(0,0,0))