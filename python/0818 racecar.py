from collections import deque
from math import copysign
class Solution:
    def racecar(self, target: int) -> int:
        """
            #bfs #google
        """
        pos = 0
        spe = 1
        # visited[(pos,spe)] = # of moves
        visited=set([(pos,spe)])
        # queue stores state (pos,spe,# of move)
        queue = deque([(0,spe)])
        cnt = 0
        while queue:
            for _ in range(len(queue)):
                pos,spe = queue.popleft()
                if pos == target:
                    return cnt
                _pos = pos + spe
                _spe = spe * 2
                if abs(_pos - target)<target and (_pos,_spe) not in visited:
                    visited.add((_pos,_spe))
                    queue.append((_pos,_spe))
                _pos = pos
                _spe = 1 if spe<0 else -1
                if (_pos,_spe) not in visited:
                    visited.add((_pos,_spe))
                    queue.append((_pos,_spe))
            cnt += 1