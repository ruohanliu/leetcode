from typing import List
from collections import deque
from sortedcontainers import SortedList
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
            #bfs

            return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.
        """
        directions = {(0,-1),(0,1),(1,0),(-1,0)}
        m = len(maze)
        n = len(maze[0])
        queue = deque([start])
        maze[start[0]][start[1]] = -1
        while queue:
            sx,sy = queue.popleft()
            startDis = maze[sx][sy]
            for dx,dy in directions:
                dis = 0
                x,y = sx,sy
                x+=dx
                y+=dy
                while (x < m and x >= 0 and y <n and y >= 0) and maze[x][y] != 1:
                    x+=dx
                    y+=dy
                    dis += 1
                x-=dx
                y-=dy
                if maze[x][y] == 0:
                    queue.append((x,y))
                    maze[x][y] = startDis - dis
                elif maze[x][y] < 0:
                    if startDis - dis > maze[x][y]:
                        maze[x][y] = startDis - dis
                        queue.append((x,y))

        if maze[destination[0]][destination[1]] == 0:
            return -1
        else:
            return -maze[destination[0]][destination[1]]-1

    def shortestDistance_dijkstra(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
            #bfs #dijkstra

            return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.
        """
        directions = {(0,-1),(0,1),(1,0),(-1,0)}
        m = len(maze)
        n = len(maze[0])
        queue = SortedList([(0,start[0],start[1])])
        while queue:
            startDis,sx,sy = queue.pop(0)
            if [sx,sy] == destination:
                return startDis
            if maze[sx][sy] == 2:
                continue
            maze[sx][sy] = 2

            for dx,dy in directions:
                dis = 0
                x,y = sx,sy
                x+=dx
                y+=dy
                while (x < m and x >= 0 and y <n and y >= 0) and maze[x][y] != 1:
                    dis += 1
                    x+=dx
                    y+=dy
                x-=dx
                y-=dy
                if maze[x][y] == 0:
                    queue.add((startDis + dis,x,y))
        return -1