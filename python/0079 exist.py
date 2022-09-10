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
            if p == k:
                return True
            visited.add((i,j))

            for di,dj in directions:
                r = i+di
                c = j+dj
                if m>r>=0<=c<n and board[r][c] == word[p] and (r,c) not in visited:
                    if dfs(r,c,p+1,visited):
                        return True

            visited.remove((i,j))
            return False
                    
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i,j,1,visited):
                    return True

        return False