from functools import cache
class Solution:
    def knightDialer(self, n: int) -> int:
        """
            #dp
        """
        @cache
        def helper(k,init = None):
            if k == 1:
                return 1
            elif init == 1:
                return (helper(k-1, 8) + helper(k-1, 6)) % mod
            elif init == 2:
                return (helper(k-1, 7) + helper(k-1, 9)) % mod
            elif init == 3:
                return (helper(k-1, 4) + helper(k-1, 8)) % mod
            elif init == 4:
                return (helper(k-1, 3) + helper(k-1, 9) + helper(k-1, 0)) % mod
            elif init == 6:
                return (helper(k-1, 1) + helper(k-1, 7) + helper(k-1, 0)) % mod
            elif init == 7:
                return (helper(k-1, 2) + helper(k-1, 6)) % mod
            elif init == 8:
                return (helper(k-1, 1) + helper(k-1, 3)) % mod
            elif init == 9:
                return (helper(k-1, 4) + helper(k-1, 2)) % mod
            elif init == 0:
                return (helper(k-1, 4) + helper(k-1, 6)) % mod

        if n == 1:
            return 10
        mod = 10**9+7
        return (helper(n, 0)+helper(n, 1)+helper(n,2)+helper(n, 3)+helper(n, 4)+helper(n,6)+helper(n, 7)+helper(n, 8)+helper(n, 9))%mod

    def knightDialer(self, N):
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)

    def knightDialer_matrix(self, N):
        """
            #matrix #adjacencymatrix
        """
        import numpy as np
        mod = 10**9 + 7
        if N == 1:
            return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res = 1
        N = N - 1
        while N:
            if N % 2:
                res = res * M % mod
            M = M * M % mod
            N >>= 1
        return int(np.sum(res)) % mod

s = Solution()
print(s.knightDialer_matrix(2))