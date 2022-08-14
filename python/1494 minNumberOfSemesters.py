class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """
            #dp #bitmask #graph
        """
        @cache
        def dp(taken,degree):
            if taken == target:
                return 0
            candidates = [i for i in range(n) if taken & 1<<i == 0 and degree[i] == 0]
            ans = float("inf")
            for candidates in combinations(candidates,min(k,len(candidates))):
                _taken,_degree = taken,list(degree)
                for v in candidates:
                    _taken |= 1 << v
                    for _v in adjList[v]:
                        _degree[_v] -= 1
                ans = min(ans,1 + dp(_taken,tuple(_degree)))
            return ans
        
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in relations:
            adjList[a-1]+= b-1,
            indegree[b-1] += 1
                          
        target = (1<<n) - 1
        return dp(0,tuple(indegree[v] for v in range(n)))

    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        @cache
        def dp(taken,degree):
            if taken == target:
                return 0
            candidates = [i for i in range(n) if taken & 1<<i == 0 and degree & (15 << i*4) == 0]
            ans = float("inf")
            for candidates in combinations(candidates,min(k,len(candidates))):
                _taken = taken
                _degree = degree
                for v in candidates:
                    _taken |= 1 << v
                    for _v in adjList[v]:
                        _degree = ~(15 << _v*4) & _degree | (_degree & 15 << _v*4)-(1 << _v*4)
                ans = min(ans,1 + dp(_taken,_degree))
            return ans
        
        adjList = defaultdict(list)
        indegree = 0
        for a,b in relations:
            adjList[a-1]+= b-1,
            indegree = ~(15 << (b-1)*4) & indegree | ((indegree & 15 << (b-1)*4) + (1 << (b-1)*4))
        target = (1<<n) - 1
        return dp(0,indegree)
