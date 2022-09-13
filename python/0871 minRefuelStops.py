class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
           #greedy #heap #google
           related: 1642 630
        """
        n = len(stations)
        dp = [0] * (n+1)
        dp[0] = startFuel
        for j, (pos,fuel) in enumerate(stations):
            for i in range(j,-1,-1):
                if dp[i] >= pos:
                    dp[i+1] = max(dp[i+1],dp[i]+fuel)
        for i,d in enumerate(dp):
            if d>=target:
                return i
        return -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        curr = startFuel
        heap = []
        ans = 0
        stations.append([target,0])
        for pos,fuel in stations:
            while pos > curr and heap:
                curr += -heapq.heappop(heap)
                ans += 1
                if curr >= target:
                    return ans
            if pos > curr:
                return -1
            heapq.heappush(heap,-fuel)
        return ans
