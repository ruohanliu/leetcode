class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
            #dp
        """    
        n = len(houses)
        houses.sort()
        cost = [[0] * n for _ in range(n)]
        for i in range(n-1):
            cost[i][i+1] = houses[i+1]-houses[i]
            j = 1
            while True:
                if i-j < 0 or i + j == n:
                    break
                cost[i-j][i+j] = cost[i-j+1][i+j-1] + houses[i+j] - houses[i-j]
                if i+j+1 < n:
                    cost[i-j][i+j+1] = cost[i-j+1][i+j] + houses[i+j+1] - houses[i-j]
                j += 1
        @cache
        def dp(i,k):
            if k == 0:
                if i == n:
                    return 0
                else:
                    return float("inf")
            ans = float("inf")
            for j in range(i,n):
                ans = min(ans,cost[i][j] + dp(j+1,k-1))
            return ans
        return dp(0,k)