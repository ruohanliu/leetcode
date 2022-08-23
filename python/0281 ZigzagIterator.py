class ZigzagIterator:
    """
        #iter
    """
    def __init__(self, v1: List[int], v2: List[int]):
        self.deque = deque()
        candidates = [v1,v2]
        for cand in candidates:
            it = iter(cand)
            if it.__length_hint__():
                self.deque.append(it)
        
    def next(self) -> int:
        val = next(self.deque[0])
        if self.deque[0].__length_hint__():
            self.deque.rotate(-1)
        else:
            self.deque.popleft()
        return val
        
    def hasNext(self) -> bool:
        return True if self.deque else False