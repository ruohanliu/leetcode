class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """
            #monostack

            You are given an array colors, in which there are three colors: 1, 2 and 3.
            You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.
        """
        n = len(colors)
        colorMap = {i:[float("inf")] * n for i in range(1,4)}
        
        dist = {i:0 for i in range(1,4)}
        for i in range(n):
            color = colors[i]
            colorMap[color][dist[color]:i+1] = reversed(range(i - dist[color]+1))
            dist[color] = i+1

        dist = {i:n-1 for i in range(1,4)}
        for i in reversed(range(n)):
            color = colors[i]
            colorMap[color][i:dist[color]+1] = map(min, zip(range(dist[color]+1-i),colorMap[color][i:dist[color]+1]))
            dist[color] = i-1
        

        return [colorMap[q[1]][q[0]] if colorMap[q[1]][q[0]] < inf else -1 for q in queries]
            