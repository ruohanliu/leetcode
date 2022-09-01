class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
            #bfs
        """
        if source == target:
            return 0
        busList = defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                busList[stop].add(i)
        cnt = 0
        queue = deque([source])
        visitedStop = set([source])
        visitedBus = set()
        while queue:
            cnt += 1
            size = len(queue)
            for _ in range(size):
                v = queue.popleft()
                for b in busList[v]:
                    if b not in visitedBus:
                        visitedBus.add(b)
                        for s in routes[b]:
                            if s not in visitedStop:
                                if s == target:
                                    return cnt
                                visitedStop.add(s)
                                queue.append(s)
        return -1