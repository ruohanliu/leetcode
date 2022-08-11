class TreeAncestor:
    """
        #binarylifting #algorithm #dp #important

        ith node's 2^j parent is ith node's 2^(j-1) parent's 2^(j-1) parent
    """
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length()
        self.dp = [[-1] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                if j == 0:
                    self.dp[i][0] = parent[i]
                elif self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while node != -1 and k:
            i = k.bit_length() - 1
            node = self.dp[node][i]
            k -= 1 << i
        return node
