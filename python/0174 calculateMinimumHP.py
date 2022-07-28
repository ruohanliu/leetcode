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
