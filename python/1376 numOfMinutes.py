class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
            #recursion #important

            Time Needed to Inform All Employees
        """
        def dfs(v):
            if not adjList[v]:
                return 0

            return max(dfs(_v) for _v in adjList[v])+informTime[v]
                
        ans = 0
        adjList = defaultdict(list)
        for v in range(n):
            adjList[manager[v]] += v,
        
        return dfs(headID)
    
    def numOfMinutes_bad(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(v,t):
            nonlocal ans
            ans = max(ans,t)
            for _v in adjList[v]:
                dfs(_v,t+informTime[v])
                
        ans = 0
        adjList = defaultdict(list)
        for v in range(n):
            adjList[manager[v]] += v,
        
        dfs(headID,0)
        return ans
        
        
        