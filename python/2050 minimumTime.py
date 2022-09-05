class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
            #dp #topologicalsort #heap #important
        """
        @cache
        def dp(v):
            # time to finish course v is its time + longest time to finish its prerequisites
            return time[v - 1] + max([dp(_v) for _v in adjList[v]],default = 0)

        adjList = defaultdict(list)
        for prev, nxt in relations:
            adjList[nxt].append(prev)
        return max(dp(v) for v in range(1, n+1))

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
            O(E + ElogV)
        """
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        for prev, nxt in relations:
            adjList[prev].append(nxt)
            indegree[nxt] += 1
        heap = [(time[v-1],v) for v in range(1,n+1) if indegree[v] == 0]
        heapq.heapify(heap)
        while heap:
            moment,v = heapq.heappop(heap)
            for _v in adjList[v]:
                indegree[_v] -= 1
                if indegree[_v] == 0:
                    heapq.heappush(heap,(moment+time[_v-1],_v))
            del adjList[v]
        return moment

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
            O(E+V)
        """
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        for prev, nxt in relations:
            adjList[prev].append(nxt)
            indegree[nxt] += 1
        queue = deque([v for v in range(1,n+1) if indegree[v] == 0])
        dp = [0] * (n+1)
        for v in queue:
            dp[v] += time[v-1]
        while queue:
            v = queue.popleft()
            for _v in adjList[v]:
                dp[_v] = max(dp[_v],dp[v]+time[_v-1])
                indegree[_v] -= 1
                if indegree[_v] == 0:
                    queue.append(_v)
            del adjList[v]
        return max(dp)