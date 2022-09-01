class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
            #bfs #astar
            heuristic must be admissible (do not overestimate future cost,it is lower bound)
        """
        state = ''.join(str(d) for row in board for d in row)
        queue = deque([state])
        seen = {state}
        steps = 0
        m = 2
        n = 3
        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                i = state.index("0")
                if state == '123450':
                    return steps
                x, y = divmod(i,n)
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if m > r >= 0 <= c < n:
                        ch = list(state)
                        ch[i], ch[r * n + c] = ch[r * n + c], ch[i]
                        _state = "".join(ch)
                        if _state not in seen:
                            seen.add(_state)
                            queue.append(_state)
            steps += 1              
        return -1