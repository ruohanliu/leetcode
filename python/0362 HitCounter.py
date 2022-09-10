class HitCounter:
    """
        #bisect #databricks

        keep historical
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


    """
        discard historical
    """
    def __init__(self):
        self.deque = collections.deque()
        self.cnt = 0

    def hit(self, timestamp):
        if self.deque and self.deque[-1][0] == timestamp:
            self.deque[-1][1] += 1
        else:
            self.deque.append([timestamp,1])
        self.cnt += 1
        
    def getHits(self, timestamp):
        # inclusive to delete
        oldTime = timestamp - 300
        while self.deque and self.deque[0][0] <= oldTime:
            self.cnt -= self.deque.popleft()[1]
        return self.cnt