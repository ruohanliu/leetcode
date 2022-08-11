class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
            #binarysearch #matrix
        """
        def test(length):
            for i in range(length,m+1):
                for j in range(length,n+1):
                    if ps[i][j] - ps[i-length][j] - ps[i][j-length] + ps[i-length][j-length] <= threshold:
                        return True
            return False

        m = len(mat)
        n = len(mat[0])
        ps = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
        
        lo = 0
        hi = min(m,n)
        while lo < hi:
            length = (lo+hi) // 2 + 1
            if test(length):
                lo = length
            else:
                hi = length - 1
        return hi


    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
            O(n)
            only works for non-negative matrix
        """
        m = len(mat)
        n = len(mat[0])
        ps = [[0] * (n+1) for _ in range(m+1)]
        length = 1
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                ps[i][j] = mat[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

                
                if i >= length and j >= length and ps[i][j] - ps[i-length][j] - ps[i][j-length] + ps[i-length][j-length] <= threshold:
                    ans = length
                    length += 1
        return ans