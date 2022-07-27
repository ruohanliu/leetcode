from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
            #matrix #divmod #gcd #math
            
            m = len(grid)
            n = len(grid[0])
            x,y = divmod(pos,n)
        """
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        N = m*n
        if k%N == 0:
            return grid

        gcd = math.gcd(N,k)
        for i in range(gcd):
            pos = i % N
            x,y = divmod(pos,n)
            temp = grid[x][y]
            for j in range(1,N//gcd+1):
                x,y = divmod((pos+j*k)%N,n)
                grid[x][y], temp = temp, grid[x][y]
        return grid
