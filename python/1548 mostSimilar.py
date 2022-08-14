class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        """
            #dijkstra #graph #multistate
        """
        m = len(targetPath)
        adjList = defaultdict(list)
        for a,b in roads:
            adjList[a].append(b)
            adjList[b].append(a)
        state = defaultdict(lambda:float("inf"))
        heap = []
        for v in range(n):
            heap.append((1 if names[v] != targetPath[0] else 0,-1,[v]))
            state[v,1] = 1 if names[v] != targetPath[0] else 0
        heapq.heapify(heap)
        while heap:
            distance,i,path = heapq.heappop(heap)
            if distance > state[path[-1],-i]:
                continue
            if -i == m:
                return path
            v = path[-1]
            for _v in adjList[v]:
                _distance = distance + (1 if names[_v] != targetPath[-i] else 0)
                if _distance < state[_v,-i+1]:
                    state[_v,-i+1] = _distance
                    heapq.heappush(heap,(_distance,i-1,(path+[_v])[:]))