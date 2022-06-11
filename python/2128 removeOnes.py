from typing import List
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        """
            #matrix
            order of row/col operations does not matter
            assuming apply row operations first, then all col are either 1's or 0's
            then all rows initially should have same column-wise pattern
        """

        complement = [x^1 for x in grid[0]]
        for j in range(1,len(grid)):
            if grid[j] != grid[0] and grid[j] != complement:
                return False
        return True