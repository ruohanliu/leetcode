class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        """
            #counter
        """
        count = Counter()
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for k in range(j+1,n):
                        if grid[i][k]:
                            ans += count[j,k]
                            count[j,k] += 1
        return ans