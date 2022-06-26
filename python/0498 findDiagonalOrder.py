from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
            #matrix #diagonal

            diagnoal index i-j = k for 0 <= i < m and 0 <= j < n
            antidiagnoal index i+j = k for 0 <= i < m and 0 <= j < n
        """
        m = len(mat)
        n = len(mat[0])
        ans = []
        for d in range(m+n-1):
            temp = []
            r = min(d,m-1)
            c = d-r
            while r>0 and c<n:
                temp += mat[r][c],
                r -= 1
                c += 1
            if r%2:
                ans.extend(temp[::-1])
            else:
                ans.extend(temp)
        return ans