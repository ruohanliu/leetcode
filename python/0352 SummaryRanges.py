class SummaryRanges:
    """
        #segmenttree #sortedlist
        related 2276
    """
    def __init__(self):
        from sortedcontainers import SortedList
        self.range = SortedList()

        
    def addNum(self, val: int) -> None:
        left = val
        right = val
        i = self.range.bisect_left([val,val])
        while i >= 1:
            x,y = self.range[i-1]
            if y + 1 < val:
                break
            left = min(val,x)
            right = max(val,y)
            self.range.pop(i-1)
            i -= 1
        while i < len(self.range):
            x,y = self.range[i]
            if x - 1 > right:
                break
            right = max(right,y)
            self.range.pop(i)
        self.range.add([left,right])

    def getIntervals(self) -> List[List[int]]:
        return [x for x in self.range]