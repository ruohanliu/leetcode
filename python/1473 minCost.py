class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
            #dp #multistate
        """
        # states: k = # of neighborhoods p = color of last house
        @cache
        def dp(i,k,p):
            if k > target:
                return float("inf")
            if i == m:
                if k == target:
                    return 0
                else:
                    return float("inf")
            
            if houses[i] == 0:
                res = float("inf")
                for c in range(1,n+1):
                    if c != p:
                        res = min(res,dp(i+1,k+1,c)+cost[i][c-1])
                    else:
                        res = min(res,dp(i+1,k,c)+cost[i][c-1])
            else:
                if houses[i] == p:
                    res = dp(i+1,k,houses[i])
                else:
                    res = dp(i+1,k+1,houses[i])
            return res

        res = dp(0,0,-1)
        return res if res < float("inf") else -1
            