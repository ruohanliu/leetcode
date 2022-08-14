from sortedcontainers import SortedList
class MyCalendarTwo:
    """
        #interval #important
        related 253 986
        O(nlogn)
    """
    def __init__(self):
        self.bookings = {}
        self.id = 0

    def _removeOverlap(self,id):
        overlap = 0
        for _,status in sorted(x for interval in self.bookings.values() for x in ((interval[0],1),(interval[1],-1))):
            overlap += status
            if overlap == 3:
                del self.bookings[id]
                return False
        return True

    def book(self, start: int, end: int) -> bool:
        self.id += 1
        self.bookings[self.id] = (start,end)
        return self._removeOverlap(self.id)

class MyCalendarTwo:
    """
        O(n)
    """
    def __init__(self):
        self.one = []
        self.two = []

    def book(self, start: int, end: int) -> bool:
        for x,y in self.two:
            if start < y and end > x:
                return False
        for x,y in self.one:
            if start < y and end > x:
                self.two.append((max(start,x),min(end,y)))
        self.one.append((start,end))
        return True

class MyCalendarTwo:
    """
        O(logn)
    """
    def __init__(self):
        from sortedcontainers import SortedList
        self.one = SortedList()
        self.two = SortedList()

    def _merge(self,sl,left,right):
        i = sl.bisect_left([left,right])
        if i - 1 >= 0:
            x,y = sl[i-1]
            if y >= left:
                left = min(x,left)
                right = max(y,right)
                sl.pop(i-1)
                i-=1
        if i < len(sl):
            x,y = sl[i]
            if right >= x:
                right = max(right,y)
                sl.pop(i)
        sl.add([left,right])
        
    def book(self, start: int, end: int) -> bool:
        i = self.two.bisect_left([start,end])
        if (i-1 >= 0 and self.two[i-1][1] > start) or (i<len(self.two) and self.two[i][0] < end):
            return False

        overlap = []
        i = self.one.bisect_left([start,end])
        minRight = start
        if i-1 >= 0:
            x,y = self.one[i-1]
            if y > start:
                minRight = min(y,end)
                overlap.append([start,minRight])

        if minRight<end:
            j = i
            while j < len(self.one):
                x,y = self.one[j]
                if x >= end:
                    break
                overlap.append([max(x,minRight),min(y,end)])
                j += 1
        
        self._merge(self.one,start,end)
        for x,y in overlap:
            self._merge(self.two,x,y)
        return True

    def __init__(self):
        self.delta = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start not in self.delta:
            self.delta[start] = 0
        if end not in self.delta:
            self.delta[end] = 0

        self.delta[start] += 1
        self.delta[end] -= 1

        peak = 0
        for d in self.delta.values():
            peak += d
            if peak >= 3:
                self.delta[start] -= 1
                self.delta[end] += 1
                return False
        return True