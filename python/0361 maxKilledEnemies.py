from typing import List
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
            #dp #matrix #important #bomb
            related #2257
            dp can be done in the inner loop at small scale
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        colKills = [0] * n
        rowKills = 0
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == "W":
                    rowKills = 0
                    for k in range(j,n):
                        if grid[i][k] == "W":
                            break
                        if grid[i][k] == "E":
                            rowKills += 1
                if i == 0 or grid[i-1][j] == "W":
                    colKills[j] = 0
                    for k in range(i,m):
                        if grid[k][j] == "W":
                            break
                        if grid[k][j] == "E":
                            colKills[j] += 1
                            
                if grid[i][j] == "0":
                    ans = max(ans,rowKills + colKills[j])
        return ans