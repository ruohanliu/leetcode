from typing import List 
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
            #interval #listcomprehension #heap
        """
        heap = []
        for interval in intervals:
            heapq.heappush(heap,(interval[0],1))
            heapq.heappush(heap,(interval[1],-1))
        
        room = 0
        ans = 0
        while heap:
            _,status = heapq.heappop(heap)
            room += status
            ans = max(ans,room)
        return ans

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        ans = 0
        for _,v in sorted(x for interval in intervals for x in ((interval[0],1),(interval[1],-1))):
            rooms += v
            ans = max(rooms,ans)
        return ans