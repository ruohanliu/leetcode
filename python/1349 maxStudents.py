from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """
            #greedy #important #graph #bipartition #hungarian #furtherstudy
            https://leetcode.com/problems/maximum-students-taking-exam/discuss/503790/Python-Hungarian-Time-O(m2*n2)-Space-O(m*n)-beat-100
            https://www.youtube.com/watch?v=Sal6kHewGcM

            related 1820
        """
        m = len(seats)
        n = len(seats[0])

        adjList = defaultdict(set)
        s = set()

        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    s.add((i, j))
                    for x, y in [(i, j - 1), (i - 1, j - 1), (i - 1, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and seats[x][y] == '.':
                            adjList[i, j].add((x, y))
                            adjList[x, y].add((i, j))
        res = 0
        while s:
            # Crucial: Find the chair which has least influence
            u = min(s, key = lambda x:len(adjList[x]))
            s.remove(u)
            res += 1
            for v in adjList[u]:
                for w in adjList[v]:
                    if w != u:
                        adjList[w].remove(v)
                s.remove(v)
                del adjList[v]
            del adjList[u]
        return res

    def maxStudents_tle(self, seats: List[List[str]]) -> int:
        """
            #dp #bitmask
        """
        # given a state, return the max # of students
        @cache
        def dp(state):
            return max((dp(state | 1 << i) for i in range(k) if state & 1 << i == 0 and not any(state & 1 << j for j in adjList[i])),default = state.bit_count())
            
            
        m = len(seats)
        n = len(seats[0])
        bit2xy = {}
        xy2bit = {}
        state = 0
        k = 0
        for i in range(m):
            for j in range(n):
                if seats[i][j] == ".":
                    bit2xy[k] = (i,j)
                    xy2bit[i,j] = k
                    k += 1
        adjList = defaultdict(list)
        for i in range(k):
            x,y = bit2xy[i]
            for dx,dy in ((0,1),(0,-1),(-1,1),(-1,-1),(1,1),(1,-1)):
                r = x+dx
                c = y+dy
                if 0<=r<m and 0<=c<n and seats[r][c] == ".":
                    adjList[i].append(xy2bit[r,c])

        return dp(state)