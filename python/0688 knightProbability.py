class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
            #simulation #dp
        """
        if row == n or column == n:
            return 0

        directions = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2))
        ans = 1
        queue = Counter()
        queue[(row,column)] = 1
        while k:
            nextQueue = Counter()
            size = len(queue)
            if size == 0:
                return 0
            cnt = 0
            for r,c in queue:
                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if 0<=row<n and 0<=col<n:
                        cnt += queue[(r,c)]
                        nextQueue[(row,col)] += queue[(r,c)]
            ans *= cnt / (queue.total() * 8)
            queue = nextQueue
            k -= 1
        return ans

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2))
        prev = [[0] * n for _ in range(n)]
        prev[row][column] = 1
        for _ in range(k):
            curr = [[0] * n for _ in range(n)]
            for r,row in enumerate(prev):
                for c,val in enumerate(row):
                    for dr,dc in directions:
                        if 0 <= r+dr < n and 0 <= c+dc < n:
                            curr[r+dr][c+dc] += val / 8.0
            
            prev = curr
        return sum(map(sum,prev))