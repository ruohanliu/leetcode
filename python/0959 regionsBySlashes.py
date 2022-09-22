class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        self.p[x] = y
        return 1

class Solution(object):
    """
        #unionfind #bfs
    """
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        ans = 4*N*N
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    ans -= dsu.union(root + 0, root + 1)
                    ans -= dsu.union(root + 2, root + 3)
                if val in '\ ':
                    ans -= dsu.union(root + 0, root + 2)
                    ans -= dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: ans -= dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: ans -= dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: ans -= dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: ans -= dsu.union(root + 1, (root-4) + 2)

        return ans

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        mapping = [[""] * n for _ in range(n)]
        seen = [[0] * n for _ in range(n)]
        for i in range(n):
            j = 0
            k = 0
            while j < len(grid[i]):
                if grid[i][j] == " ":
                    pass
                elif grid[i][j] == "/":
                    mapping[i][k] = "/"
                else:
                    mapping[i][k] = "|"
                j+=1
                k+=1

        directions = [((0,-1),(0,1),(1,0),(-1,0)),\
                      ((0,1),(1,0)), #rd
                      ((0,1),(-1,0)), #ru
                      ((0,-1),(1,0)), #ld
                      ((0,-1),(-1,0)) #lu
                     ]
        def bfs(i,j,side):
            # 1 ~ left
            # 2 ~ right
            queue = deque([(i,j,side)])
            seen[i][j] |= side
            while queue:
                i,j,side = queue.popleft()
                if side == 3:
                    d = directions[0]
                elif side == 1 and mapping[i][j] == "|":
                    d = directions[3]
                elif side == 1 and mapping[i][j] == "/":
                    d = directions[4]
                elif side == 2 and mapping[i][j] == "|":
                    d = directions[2]
                elif side == 2 and mapping[i][j] == "/":
                    d = directions[1]
                for di,dj in d:
                    r = i+di
                    c = j+dj
                    if n>r>=0<=c<n and seen[r][c] != 3:
                        if mapping[r][c] == "":
                            seen[r][c] = 3
                            queue.append((r,c,3))
                        elif ((mapping[r][c] == "/" and (di == 1 or dj == 1)) or \
                              (mapping[r][c] == "|" and (di == -1 or dj == 1))) and seen[r][c] != 1:
                            seen[r][c] |= 1
                            queue.append((r,c,1))
                        elif ((mapping[r][c] == "/" and (di == -1 or dj == -1)) or \
                              (mapping[r][c] == "|" and (di == 1 or dj == -1))) and seen[r][c] != 2:
                            seen[r][c] |= 2
                            queue.append((r,c,2))
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if seen[i][j] < 3:
                    if mapping[i][j] == "":
                        bfs(i,j,3)
                        ans += 1
                    else:
                        if not (seen[i][j] & 1):
                            bfs(i,j,1)
                            ans += 1
                        if not (seen[i][j] & 2):
                            bfs(i,j,2)
                            ans += 1
        return ans