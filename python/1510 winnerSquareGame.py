class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
            #dp #game
        """
        @cache
        def game(i):
            nonlocal n
            if i >= n:
                return False
            for j in range(1,math.isqrt(n-i)+1):
                if not game(i+j*j):
                    return True
            return False
        
        return game(0)

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in reversed(range(n)):
            for k in range(1,math.isqrt(n-i)+1):
                if dp[i+k*k] == False:
                    dp[i] = True
                    break
        return dp[0]