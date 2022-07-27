from sortedcontainers import SortedList
class MyCalendarTwo:
    """
        #segmenttree #todo

        https://leetcode.com/problems/my-calendar-ii/discuss/109528/nlogd-Java-solution-using-segment-tree-with-lazy-propagation-(for-the-general-case-of-K-booking)
    """

    def __init__(self):
        self.c = SortedList()

    def book(self, start: int, end: int) -> bool:
        cnt = 0
        for booking in self.c:
            if booking[1] <= start:
                continue
            elif booking[0] >= end:
                break
            else:
                cnt += 1
        
        if cnt < 2:
            self.c.add((start,end))
            return True
        else:
            return False