class HitCounter:
    """
        #bisect
    """
    def __init__(self):
        self.ps = [[float("-inf"),0]]

    def hit(self, timestamp: int) -> None:
        if timestamp == self.ps[-1]:
            self.ps[-1][1] += 1
        else:
            self.ps.append([timestamp,self.ps[-1][1]+1])

    def getHits(self, timestamp: int) -> int:
        j = bisect.bisect_right(self.ps,[timestamp,float("inf")])-1
        i = bisect.bisect_right(self.ps,[timestamp-300,float("inf")])-1
        return self.ps[j][1] - self.ps[i][1]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)