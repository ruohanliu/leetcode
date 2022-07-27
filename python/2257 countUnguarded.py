from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
            #dp #matrix
            related #361
            dp can be done in the inner loop at small scale
        """
        ans = 0
        grid = [["0"] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = "G"
        for x, y in walls:
            grid[x][y] = "W"

        colGuarded = [False]*n
        rowGuarded = False
        for r in range(m):
            for c in range(n):
                if c == 0 or grid[r][c-1] == "W":
                    rowGuarded = False
                    for k in range(c, n):
                        if grid[r][k] == "W":
                            break
                        elif grid[r][k] == "G":
                            rowGuarded = True
                            break

                if r == 0 or grid[r-1][c] == "W":
                    colGuarded[c] = False
                    for k in range(r, m):
                        if grid[k][c] == "W":
                            break
                        elif grid[k][c] == "G":
                            colGuarded[c] = True
                            break

                if grid[r][c] == "0":
                    ans += not (rowGuarded or colGuarded[c])

        return ans
