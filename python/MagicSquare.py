"""
    #backtrack #google
"""

def myrow(pos, n):
    # Returns a list of indices of all elements in the row containing position
    output = []
    pos = pos % n
    return list(range(pos,n**2,n))
    
def mycol(pos, n):
    # Returns a list of indices of all elements in the column containing position
    output = []
    pos = (pos // n)*n
    return list(range(pos, pos +n))

def top_diagonal(n):
    # Returns a list of indices of all elements in the top left to bottom right diagonal
    return [i*n + i for i in range(n)]

def other_diagonal(n):
    # Returns a list of indices of all elements in top right to bottom left diagonal
    return [i*n + n - i - 1 for i in range(n)]

def issafe(board, pos, x, n):
    # Returns True if x can be placed on the board
    global global_sum
    if(board[pos] is not None):
        return False
    if(x in board):
        return False
    if(pos == myrow(pos, n)[-1]):
        if(x + sum([board[r] for r in myrow(pos, n)[:-1]]) != global_sum):
            return False
    if(pos == mycol(pos, n)[-1]):
        if(x + sum([board[r] for r in mycol(pos, n)[:-1]]) != global_sum):
            return False
    if(pos == top_diagonal(n)[-1]):
        if(x + sum([board[r] for r in top_diagonal(n)[:-1]]) != global_sum):
            return False
    if(pos == other_diagonal(n)[-1]):
        if(x + sum([board[r] for r in other_diagonal(n)[:-1]]) != global_sum):
            return False
    return True

def fill(board, pos, n):
    #Backtracking through the board
    if(pos >= n**2):
        return True
    for num in range(1, n**2+1):
        if(issafe(board, pos, num, n)):
            board[pos] = num
            if(fill(board, pos+1, n)):
                return True
            else:
                board[pos] = None
    return False

n = 3
global_sum = n*(n**2+1)/2
board = [None]*(n**2)
val = fill(board, 0, n)
output = []
for i in range(n):
    output.append(board[i*n:i*n+n])
print(output)
print(val)