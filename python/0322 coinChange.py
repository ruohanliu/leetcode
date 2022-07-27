from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            #dp #knapsack

            0-1 knapsack problem. DP: O(nW) time and O(W) space

        """
        # dp[i] denotes the least number of coins for a given amount
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for m in range(coin,amount+1):
                dp[m] = min(dp[m],dp[m-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            #dijkstra
        """
        heap = [(0,0)]
        dist = [inf] * (amount + 1)
        for coin in coins:
            k = amount // coin
            cnt = 0
            for j in reversed(range(k*3//4,k)):
                mnt = j*coin
                dist[mnt] = min(dist[mnt],j)
                heap.append((dist[mnt],mnt))
                cnt +=1
                if cnt > 15:
                    break
        heapq.heapify(heap)
                
        while heap:
            cost,mnt = heapq.heappop(heap)
            if mnt == amount:
                return cost
            if cost > dist[mnt]: continue
            for coin in coins:
                _cost = cost + 1
                _mnt = mnt + coin
                if _mnt <= amount and _cost < dist[_mnt]:
                    dist[_mnt] = _cost
                    heapq.heappush(heap,(_cost,_mnt))
        return -1