class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        """
            undirected reduced adjlist

            The confusion score of the maze is the number of different cycles of length 3. Return the confusion score of the maze.
        """
        adjList = {v:set() for v in range(1,n+1)}
        for a,b in corridors:
            adjList[min(a,b)].add(max(a,b))
        
        ans = 0
        for i in range(1,n+1):
            for j in adjList[i]:
                for k in adjList[j]:
                    ans += 1 if k in adjList[i] else 0
        return ans

    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        """
            count number of cycle by couting set union
        """
        ans = 0
        adjList = {v:set() for v in range(1,n+1)}
        for a,b in corridors:
            ans += len(adjList[a]&adjList[b])
            adjList[a].add(b)
            adjList[b].add(a)
        return ans