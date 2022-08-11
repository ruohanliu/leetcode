class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
            #dp #game
        """
        @cache
        def game(i,m):
            if i >= n:
                return 0
            if n - i <= 2*m:
                return sum(piles[i:])
            ans = 0
            for j in range(1,2*m+1):
                ans = max(ans,piles[i:i+j] - game(j+1,max(m,j)))
            return ans
        
        n = len(piles)
        return (game(0,1) + sum(piles)) // 2