class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
            #matrix #dp
        """
        m = len(matrix)
        n = len(matrix[0])
        curr = matrix[0][:]+[float("inf")]
        for i in range(1,m):
            temp = float("inf")
            for j in range(n):
                temp,curr[j] = curr[j],min(temp,curr[j],curr[j+1]) + matrix[i][j]
        return min(curr)