from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            #backtrack #dfs #matrix

            Given an m x n grid of characters board and a string word, return true if word exists in the grid.
        """
        m = len(board)
        n = len(board[0])
        k = len(word)
        directions = {(-1,0),(1,0),(0,1),(0,-1)}
        visited = set()

        def dfs(i,j,p,visited):
            p += 1
            if p == k:
                return True
            visited.add((i,j))

            result = False 
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                if ni < m and ni >= 0 and nj >=0 and nj < n and board[ni][nj] == word[p] and (ni,nj) not in visited:
                    result |= dfs(ni,nj,p,visited)

            visited.remove((i,j))
            return result
                    
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i,j,0,visited):
                    return True

        return False