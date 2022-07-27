class MedianFinder:
    """
        #sortedlist
    """
    from sortedcontainers import SortedList
    def __init__(self):
        self.sl = SortedList()

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        if len(self.sl) % 2:
            return self.sl[len(self.sl)//2]
        else:
            return (self.sl[len(self.sl)//2]+self.sl[len(self.sl)//2-1]) / 2

class MedianFinder:
    """
        #heap #important
    """
    def __init__(self):
        # max heap
        self.small = []

        #min heap
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small or num < -self.small[0]:
            heapq.heappush(self.small,-num)
            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large,-heapq.heappop(self.small))
        elif not self.large or num > self.large[0]:
            heapq.heappush(self.large,num)
            if len(self.large) > len(self.small):
                heapq.heappush(self.small,-heapq.heappop(self.large))
        else:
            if len(self.large) == len(self.small):
                heapq.heappush(self.small,-num)
            else:
                heapq.heappush(self.large,num)

    def findMedian(self) -> float:
        if not self.small:
            return None
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2
