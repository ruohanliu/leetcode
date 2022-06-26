from typing import List
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
            #bfs
            
            return true if the ball can stop at the destination, otherwise return false
        """
        directions = {(0,-1),(0,1),(1,0),(-1,0)}
        m = len(maze)
        n = len(maze[0])
        queue = deque([start])
        while queue:
            sx,sy = queue.popleft()
            maze[sx][sy] = 2
            for dx,dy in directions:
                x,y = sx,sy
                x+=dx
                y+=dy
                while (x < m and x >= 0 and y <n and y >= 0) and maze[x][y] != 1:
                    x+=dx
                    y+=dy
                x-=dx
                y-=dy
                if maze[x][y] == 0:
                    if [x,y] == destination:
                        return True
                    queue.append((x,y))
        return False