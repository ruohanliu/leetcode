class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            #bfs
        """
        m = len(heights)
        n = len(heights[0])
        d = ((-1,0),(1,0),(0,-1),(0,1))
        pacific = [(r,0) for r in range(m)] + [(0,c) for c in range(1,n)]
        atlantic = [(r,n-1) for r in range(m)] + [(m-1,c) for c in range(0,n-1)]

        visitedP = set(pacific)
        visitedA = set(atlantic)

        while pacific:
            i,j = pacific.pop()
            for di,dj in d:
                r = i + di
                c = j + dj
                if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= heights[i][j] and (r,c) not in visitedP:
                    visitedP.add((r,c))
                    pacific.append((r,c))

        while atlantic:
            i,j = atlantic.pop()
            for di,dj in d:
                r = i + di
                c = j + dj
                if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= heights[i][j] and (r,c) not in visitedA:
                    visitedA.add((r,c))
                    atlantic.append((r,c))

        return list(list(x) for x in visitedA & visitedP)
