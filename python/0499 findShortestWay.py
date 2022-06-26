from typing import List
from sortedcontainers import SortedList
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """
            #bfs #dijkstra #important

            return the lexicographically minimum instruction. If the ball can't drop in the hole, return "impossible".
        """
        directions = [(0,-1,"l"),(0,1,"r"),(1,0,"d"),(-1,0,"u")]
        m = len(maze)
        n = len(maze[0])
        queue = SortedList([(0,ball[0],ball[1],"")])
        res = []
        minDistance = float("inf")
        while queue:
            startDis,sx,sy,ins = queue.pop(0)
            if maze[sx][sy] == 2:
                continue

            maze[sx][sy] = 2
            
            if startDis >=  minDistance:
                break

            for dx,dy,step in directions:
                dis = 0
                success = False
                x,y = sx,sy
                x+=dx
                y+=dy
                while (x < m and x >= 0 and y <n and y >= 0) and maze[x][y] != 1:
                    dis += 1
                    if [x,y] == hole:
                        if startDis+dis<minDistance:
                            minDistance = startDis+dis
                            res.clear()
                            res += (ins+step),
                        elif startDis+dis == minDistance:
                            res += (ins+step),
                        success = True
                        break
                    x+=dx
                    y+=dy
                if success: break
                x-=dx
                y-=dy
                if maze[x][y] == 0:
                    queue.add((startDis + dis,x,y,ins+step))
        return sorted(res)[0] if res else "impossible"