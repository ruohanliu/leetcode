from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
            #matrix #zip

            zip object is not subscriptable

            Given an m x n binary matrix mat, return the number of special positions in mat.
            A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
        """
        m = len(mat)
        n = len(mat[0])
        goodRow = set()
        goodCol = set()
        for i in range(m):
            cnt = 0
            for j in range(n):
                if mat[i][j] == 1:
                    cnt += 1
            if cnt == 1:
                goodRow.add(i)
                
        for j in range(n):
            cnt = 0
            for i in range(m):
                if mat[i][j] == 1:
                    cnt += 1
            if cnt == 1:
                goodCol.add(j)
                
        return sum(mat[i][j] for i in goodRow for j in goodCol)

    def numSpecial(self, mat: List[List[int]]) -> int:
        """
            #matrix #zip
        """
        goodRow = [i for i in range(len(mat)) if sum(mat[i]) == 1]
        goodCol = [j for j in range(len(mat[0])) if sum(list(zip(*mat))[j]) == 1]
                
        return sum(mat[i][j] for i in goodRow for j in goodCol)