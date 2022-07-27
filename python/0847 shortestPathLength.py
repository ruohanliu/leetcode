from typing import List
from collections import defaultdict,deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
            #graph #hard #bfs #2n
            
            fixed weight edge: no need for heap or recording cost
        """
        n = len(graph)
        target = (1<<n) - 1

        # optimal path must start with a leaf
        degree = defaultdict(int)
        for a,nodes in enumerate(graph):
            for b in nodes:
                degree[a]+=1
                degree[b]+=1
        queue = deque([(v,1<<v) for v in range(n) if degree[v] == 1])
        del degree
        if not queue:
            queue = deque([(v,1<<v) for v in range(n)])

        step = 0        
        states = defaultdict(set)
        for v,state in queue:
            states[v].add(state)
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                v,state = queue.popleft()
                for _v in graph[v]:
                    _state = state | (1<<_v)
                    if _state == target:
                        return step
                    # optionally we could require that (_state ^ state_) & _state
                    if _state not in states[_v]:
                        states[_v].add(_state)
                        queue.append((_v,_state))
        return 0