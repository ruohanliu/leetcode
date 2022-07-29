class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
            #dp
        """
        n = len(costs)
        k = len(costs[0])
        curr = [(cost,idx) for idx,cost in enumerate(costs[0])]
        for i in range(1,n):
            heapq.heapify(curr)
            cost1,color1 = curr[0]
            cost2,color2 = curr[1] if k == 2 or curr[1][0] < curr[2][0] else curr[2]
            for color in range(k):
                curr[color] = ((cost1 if color != color1 else cost2) + costs[i][color],color)
                
        return min(cost for cost,color in curr)

    def minCostII(self, costs: List[List[int]]) -> int:
        """
            #dp #optimized
        """
        def heappush(heap,item):
            if len(heap) < 2:
                heapq.heappush(heap,item)
            else:
                heapq.heappushpop(heap,item)

        n = len(costs)
        k = len(costs[0])
        prev = []
        for idx,cost in enumerate(costs[0]):
            heappush(prev,(-cost,idx))
        for i in range(1,n):
            curr = []
            for color in range(k):
                heappush(curr,((prev[1][0] if color != prev[1][1] else prev[0][0]) - costs[i][color],color))
            prev,curr = curr,prev
                
        return min(-cost for cost,_ in prev)