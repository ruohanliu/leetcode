from sortedcontainers import SortedDict
class MyCalendarThree:
    """
        #sorteddict #interval

        cannot use maintain interval in sortedlist because there cuold be multiple overlap

        O(nlogn)
    """
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
        k = 0
        for status in self.delta.values():
            peak += status
            k = max(k,peak)
        return k