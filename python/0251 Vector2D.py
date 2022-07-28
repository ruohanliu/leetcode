class Vector2D:
    """
        #iter
    """
    def __init__(self, vec: List[List[int]]):
        self.V = vec
        self.more = False
        self.m = self.n = None
        for i in range(len(self.V)):
            if len(self.V[i]):
                self.m = i
                self.n = 0
                self.more = True
                break

    def next(self) -> int:
        val = self.V[self.m][self.n]
        more = False
        self.n += 1
        for i in range(self.m,len(self.V)):
            for j in range(self.n,len(self.V[i])):
                self.m = i
                more = True
                break
            if more:
                break
            self.n = 0
        self.more = more
        return val

    def hasNext(self) -> bool:
        return self.more