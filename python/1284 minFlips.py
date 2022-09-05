class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        """
            #backtrack #bruteforce
        """
        m, n = len(mat), len(mat[0])
        def flip(i, j):
            for i, j in (i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= i < m and 0 <= j < n:
                    mat[i][j] ^= 1
        possible = set()
        # row by row, when reached last row, all cell should be 0
        def backtrack(i, j, flips):
            if j == n:
                i, j = i+1, 0
            if i == m:
                if max(mat[-1]) == 0:
                    possible.add(flips)
                return
            if i == 0 or mat[i-1][j] == 0:
                backtrack(i, j+1, flips)
            if i == 0 or mat[i-1][j] == 1:
                flip(i, j)
                backtrack(i, j+1, flips+1)
                flip(i, j)
        backtrack(0, 0, 0)
        return min(possible, default=-1)