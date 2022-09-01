class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
            #dijkstra #astar #important
            add a total cost estimation to the heap, with higher prority than steps so far
            total cost est = cost so far + estimated future cost (lower bound)
        """
        def dist(i,j):
            return target[0]-i + target[1]-j
        m = len(grid)
        n = len(grid[0])
        target = (m-1,n-1)
        heap = [(dist(0,0),0,0,0,k)]
        seen = set([(0,0,k)])
        while heap:
            est,steps,i,j,k = heapq.heappop(heap)
            if est - steps <= k:
                return est
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                r = i+di
                c = j+dj
                if 0<=r<m and 0<=c<n:
                    _k = k - grid[r][c]
                    state = (r,c,_k)
                    if _k >= 0 and state not in seen:
                        seen.add(state)
                        _est = dist(r,c) + steps + 1
                        heapq.heappush(heap,(_est,steps+1,r,c,_k))
        return -1