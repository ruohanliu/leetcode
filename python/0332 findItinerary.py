from audioop import reverse


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(v):
            nonlocal route,visited,ans
            if len(route) == len(tickets)+1:
                ans = route[:]
                return True
            
            for i,_v in enumerate(adjList[v]):
                if not visited[v][i]:
                    visited[v][i] = True
                    route.append(_v)
                    if backtrack(_v):
                        return True
                    route.pop()
                    visited[v][i] = False
            return False
                
        adjList = defaultdict(list)
        visited = defaultdict(list)
        for a,b in tickets:
            adjList[a].append(b)
            visited[a].append(False)
        
        for a in adjList:
            adjList[a].sort()
        
        ans = []
        route = ["JFK"]
        backtrack("JFK")
        return ans

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
            #Eulerian #important
        """
        def dfs(v):
            nonlocal ans
            while adjList[v]:
                _v = adjList[v].pop()
                dfs(_v)
            ans.append(v)

        adjList = defaultdict(list)
        for a,b in tickets:
            adjList[a].append(b)
        
        for a in adjList:
            adjList[a].sort(reverse = True)
        
        ans = []
        dfs("JFK")
        return ans[::-1]