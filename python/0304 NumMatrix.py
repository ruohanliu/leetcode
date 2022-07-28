class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.dp[i][j]= matrix[i-1][j-1]+self.dp[i-1][j]+self.dp[i][j-1]-self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

    """
        #fenwicktree
    """
    def __init__(self, matrix: List[List[int]]):
        """
            efficient init
        """
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix
        self.bit = [[0]*(n+1)] + [[0] + matrix[r] for r in range(m)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                pi = i+(i&-i)
                pj = j+(j&-j)
                if pi < m+1:
                    self.bit[pi][j] += self.bit[i][j]
                if pj < n+1:
                    self.bit[i][pj] += self.bit[i][j]
                if pi < m+1 and pj < n+1:
                    self.bit[pi][pj] -= self.bit[i][j]

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = [[0] * n for _ in range(m)]
        self.bit = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                self.update(i,j,matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i < len(self.bit):
            j = col + 1
            while j < len(self.bit[0]):
                self.bit[i][j] += delta
                j += j&-j
            i += i&-i

    def query(self, row: int, col: int) -> int:
        res = 0
        i = row + 1
        while i:
            j = col+1
            while j:
                res += self.bit[i][j]
                j -= j&-j
            i -= i&-i
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.query(row2,col2) - self.query(row2,col1-1) - self.query(row1-1,col2) + self.query(row1-1,col1-1)