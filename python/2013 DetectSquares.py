class DetectSquares:
    """
        #defaultdict
        2nd layer must be initialized with = first
    """

    def __init__(self):
        self.h = defaultdict(defaultdict)
        self.v = defaultdict(defaultdict)

    def add(self, point: List[int]) -> None:
        x,y = point
        if y in self.h[x]:
            self.h[x][y] +=1
        else:
            self.h[x][y] = 1
        if x in self.v[y]:
            self.v[y][x] +=1
        else:
            self.v[y][x] =1

    def count(self, point: List[int]) -> int:
        x,y = point
        ans = 0
        for _y in self.h[x]:
            if _y != y:
                for _x in self.v[_y]:
                    if _x in self.v[y] and abs(_x - x) == abs(y - _y):
                        ans += self.v[_y][_x] * self.h[x][_y] * self.v[y][_x]
        return ans