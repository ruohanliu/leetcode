from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
            #matrix #diagonal

            diagnoal index i-j = k for 0 <= i < m and 0 <= j < n
            antidiagnoal index i+j = k for 0 <= i < m and 0 <= j < n
        """
        board = [[0 for i in range(3)] for i in range(3)]
        cnt = 0
        def check(i,j):
            nonlocal board
            a = b = c = d = 0
            for x in range(3):
                a += board[i][(j+x)%3]
                b += board[(i+x)%3][j]
                if i-j == 0:
                    c += board[((j+x)%3+i-j)%3][(j+x)%3]
                if i+j == 2:
                    d += board[(i+x)%3][(i+j - (i+x)%3)%3]
            if a == 6 or b == 6 or c == 6 or d == 6:
                return "B"
            if a == 15 or b == 15 or c == 15 or d == 15:
                return "A"
            return "Pending"
        for i,m in enumerate(moves):
            board[m[0]][m[1]] = 2 if cnt else 5
            cnt =  1 if cnt == 0 else 0
            res = check(m[0],m[1])
            if res != "Pending":
                return res
            if i == len(moves) - 1:
                if i == 8:
                    return "Draw"
                else:
                    return "Pending"
