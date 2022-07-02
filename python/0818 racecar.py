from collections import deque
from math import copysign
class Solution:
    def racecar(self, target: int) -> int:
        """
            #bfs
        """
        pos = 0
        spe = 1
        # visited[(pos,spe)] = # of moves
        visited={(pos,spe):0}
        # queue stores state (pos,spe,# of move)
        queue = deque([(0,spe,0)])
        while queue:
            pos,spe,n = queue.popleft()
            if pos == target:
                return n
            _pos = pos + spe
            _spe = spe * 2
            if abs(_pos - target)<target and (_pos,_spe) not in visited:
                visited[(_pos,_spe)] = n+1
                queue.append((_pos,_spe,n+1))
            _pos = pos
            _spe = 1 if spe<0 else -1
            if (_pos,_spe) not in visited:
                visited[(_pos,_spe)] = n+1
                queue.append((_pos,_spe,n+1))

