class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
            #topologicalsort
        """
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in relations:
            adjList[a]+= b,
            indegree[b]+=1

        ans = 0
        queue = deque([v for v in range(1,n+1) if indegree[v] == 0])
        while queue:
            size = len(queue)
            ans +=1
            for _ in range(size):
                v = queue.popleft()
                for _v in adjList[v]:
                    indegree[_v] -= 1
                    if indegree[_v] == 0:
                        queue.append(_v)
                del adjList[v]

        return ans if not adjList else -1