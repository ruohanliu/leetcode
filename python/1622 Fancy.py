class Fancy:
    """
        #math #mod
    """
    def __init__(self):
        self.x = []
        self.a = 1
        self.b = 0
        self.mod = 10**9+7

    def append(self, val: int) -> None:
        self.x.append((val-self.b)*pow(self.a,-1,self.mod))

    def addAll(self, inc: int) -> None:
        self.b += inc

    def multAll(self, m: int) -> None:
        self.a *= m
        self.b *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.x):
            return -1
        return (self.a*self.x[idx]+self.b) % self.mod