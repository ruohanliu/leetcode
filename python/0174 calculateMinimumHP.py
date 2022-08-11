class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
            #dp #dijkstra
        """
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:
            return max(-dungeon[0][0],0) + 1
        
        minHPHistory = [[float("-inf")] * n for _ in range(m)]
        HPHistory = [[float("-inf")] * n for _ in range(m)]
        
        heap = [(-dungeon[0][0],-dungeon[0][0],0,0)]
        directions = ((0,1),(1,0))
        
        while heap:
            minHP,HP,i,j = heapq.heappop(heap)
            minHP *= -1
            HP *= -1
            if minHP < minHPHistory[i][j] and HP < HPHistory[i][j]:
                continue
            if (i,j) == (m-1,n-1):
                return max(-minHP,0)+1
            for di,dj in directions:
                r = i+di
                c = j+dj
                if 0 <= r < m and 0 <= c < n:
                    _HP = HP + dungeon[r][c]
                    _minHP = min(minHP,_HP)
                    if _minHP > minHPHistory[r][c]:
                        minHPHistory[r][c] = _minHP
                        heapq.heappush(heap,(-_minHP,-_HP,r,c))
                    if _HP > HPHistory[r][c]:
                        HPHistory[r][c] = _HP
                        heapq.heappush(heap,(-_minHP,-_HP,r,c))

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float("inf")] * n for _ in range(m)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                curr = dungeon[i][j]
                r = float("inf") if j == n-1 else max(1,dp[i][j+1]-curr)
                d = float("inf") if i == m-1 else max(1,dp[i+1][j]-curr)
                dp[i][j] = min(r,d) if min(r,d) < float("inf") else 1 - min(curr,0)
        return dp[0][0]
