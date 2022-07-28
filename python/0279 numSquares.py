import math,heapq
class Solution:
    def numSquares(self, n: int) -> int:
        """
            #dp
        """
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]

    def numSquares(self, n: int) -> int:
        """
            #dijkstra
        """
        dist = [float("inf")] * (n+1)
        heap = []
        for i in range(math.isqrt(n)+1):
            iSquare = i ** 2
            dist[iSquare] = 1
            heap.append((1,n-iSquare))
        heapq.heapify(heap)

        while heap:
            cost,remain = heapq.heappop(heap)
            if remain == 0:
                return cost
            if dist[remain] == 1:
                return cost + 1
            if cost > dist[n-remain]:
                continue
            maxSqrt = math.isqrt(remain)
            for candidate in range(1,maxSqrt+1):
                _remain = remain-candidate**2
                if cost+1 < dist[n-_remain]:
                    dist[n-_remain] = cost+1
                    heapq.heappush(heap,(cost+1,_remain))