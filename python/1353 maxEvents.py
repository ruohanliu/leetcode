class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
            #schedule #important #greedy
        """
        ans = 0
        events.sort(reverse = True)
        # heap stores event endtime
        heap = []
        while heap or events:
            if not heap:
                curr = events[-1][0]
            # push all events starting before curr to heap
            while events and events[-1][0] <= curr:
                heapq.heappush(heap,events.pop()[1])
            # greedily attend the soonest ending event on the heap
            heapq.heappop(heap)
            ans += 1
            curr += 1
            # discard any event that cannot be attended
            while heap and heap[0] < curr:
                heapq.heappop(heap)
        return ans