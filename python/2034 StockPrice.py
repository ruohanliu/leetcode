from sortedcontainers import SortedDict
class StockPrice:
    """
        #SortedDict

        peekitem() index()
    """

    def __init__(self):
        self.timePrice = {}
        self.priceFreq = SortedDict()
        self.currTime = float("-inf")

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePrice:
            self.priceFreq[self.timePrice[timestamp]] -=1
            if self.priceFreq[self.timePrice[timestamp]] == 0:
                del self.priceFreq[self.timePrice[timestamp]]
        self.timePrice[timestamp] = price
        if price not in self.priceFreq:
            self.priceFreq[price] = 1
        else:
            self.priceFreq[price] += 1
        self.currTime = max(self.currTime,timestamp)

    def current(self) -> int:
        return self.timePrice[self.currTime]

    def maximum(self) -> int:
        return self.priceFreq.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.priceFreq.peekitem(0)[0]