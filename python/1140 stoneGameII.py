class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
            #dp #game
        """
        @cache
        def game(i,m):
            nonlocal n,prefixSums
            if i >= n:
                return 0
            if n - i <= 2*m:
                return prefixSums[-1] - prefixSums[i]
            ans = float("-inf")
            for j in range(1,2*m+1):
                ans = max(ans,prefixSums[i+j] - prefixSums[i] - game(i+j,max(m,j)))
            return ans
        
        n = len(piles)
        prefixSums = list(accumulate([0]+piles))
        return (game(0,1) + sum(piles)) // 2