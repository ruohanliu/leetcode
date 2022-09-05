class TreeAncestor:
    """
        #binarylifting #algorithm #dp #important

        ith node's 2^j parent is ith node's 2^(j-1) parent's 2^(j-1) parent

        related 2277
    """
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length()
        self.dp = [[-1]*m for _ in range(n)]
        for bit in range(m):
            for i in range(n):
                if bit == 0:
                    self.dp[i][0] = parent[i]
                elif self.dp[i][bit-1] != -1:
                    self.dp[i][bit] = self.dp[self.dp[i][bit-1]][bit-1]
                    
    def getKthAncestor(self, node: int, k: int) -> int:
        while node != -1 and k:
            bit = k.bit_length() - 1
            node = self.dp[node][bit]
            k -= 1 << bit
        return node