class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
            #dfs #topologicalsort #google
        """
        def isLeaf(i,j):
            return not any(0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj] > matrix[i][j] for di,dj in d)

        m = len(matrix)
        n = len(matrix[0])
        d = ((0,1),(0,-1),(1,0),(-1,0))
        leaves = set()
        for i in range(m):
            for j in range(n):
                if isLeaf(i,j):
                    leaves.add((i,j))

        ans = 0
        while leaves:
            ans += 1
            nextLeaves = set()
            prev = {}
            for i,j in leaves:
                prev[(i,j)],matrix[i][j] = matrix[i][j],float("-inf")
            while leaves:
                i,j = leaves.pop()
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if 0<=r<m and 0<=c<n and prev[(i,j)] > matrix[r][c] > float("-inf") and isLeaf(r,c):
                        nextLeaves.add((r,c))
            leaves = nextLeaves

        return ans

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))