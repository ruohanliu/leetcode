class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
            #sudoku #backtrack
        """
        def place_number(row, col, d):
            rows[row].add(d)
            columns[col].add(d)
            boxes[box_index(row, col)].add(d)
            board[row][col] = str(d)
            
        def remove_number(row, col, d):
            """
            Remove a number which didn't lead 
            to a solution
            """
            rows[row].discard(d)
            columns[col].discard(d)
            boxes[box_index(row, col)].discard(d)
            board[row][col] = '.'  
            
        def is_valid(r,c,d):
            return not (d in rows[r] or d in columns[c] or d in boxes[box_index(r,c)])
        
        def backtrack():
            if not empty:
                return True
            r,c = empty.pop()
            for d in range(1,10):
                if is_valid(r,c,d):
                    place_number(r,c,d)
                    if backtrack():
                        return True
                    remove_number(r,c,d)
            empty.append((r,c))

        box_index = lambda row, col: (row // 3 ) * 3 + col // 3
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r,c))
                else:
                    d = int(board[r][c])
                    place_number(r,c,d)
        backtrack()