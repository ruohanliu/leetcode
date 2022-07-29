class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        curr = costs[0][:]
        for i in range(1,n):
            curr[0],curr[1],curr[2] = \
                min(curr[1],curr[2])+costs[i][0],\
                min(curr[0],curr[2])+costs[i][1],\
                min(curr[0],curr[1])+costs[i][2]
        return min(curr)