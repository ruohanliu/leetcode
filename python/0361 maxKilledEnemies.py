from typing import List
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
            #dp #matrix #important
            related #2257
            dp can be done in the inner loop at small scale
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0

        colHits = [0]*n
        rowHits = 0
        for r in range(m):
            for c in range(n):
                if c == 0 or grid[r][c-1] == "W":
                    rowHits = 0
                    for k in range(c, n):
                        if grid[r][k] == "W":
                            break
                        elif grid[r][k] == "E":
                            rowHits += 1

                if r == 0 or grid[r-1][c] == "W":
                    colHits[c] = 0
                    for k in range(r, m):
                        if grid[k][c] == "W":
                            break
                        elif grid[k][c] == "E":
                            colHits[c] += 1

                if grid[r][c] == "0":
                    total = rowHits + colHits[c]
                    ans = max(ans, total)

        return ans
