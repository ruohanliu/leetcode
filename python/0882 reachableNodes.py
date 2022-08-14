class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """
            #dijkstra #graph
        """
        adjList = defaultdict(dict)
        for a,b,cnt in edges:
            adjList[a][b] = adjList[b][a] = cnt
        state = [-1] * n
        state[0] = maxMoves
        heap = [(-maxMoves,0)]
            
        partial = defaultdict(int)
        ans = 0
        while heap:
            remain,v = heapq.heappop(heap)
            remain  = -remain
            if remain < state[v]:
                continue
            ans += 1
            for _v,cnt in adjList[v].items():
                partial[v,_v] = min(cnt,remain)
                if remain >= cnt+1:
                    _remain = remain - cnt - 1
                    if _remain > state[_v]:
                        state[_v] = _remain
                        heapq.heappush(heap,(-_remain,_v))

        return ans + sum(min(partial[a,b]+partial[b,a],cnt) for a,b,cnt in edges)