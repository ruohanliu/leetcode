class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
            #greedy #heap
            similar to #646 Maximum Length of Pair Chain
            related: 871 1642
        """
        curr = 0
        # stores the taken course
        heap = []
        courses.sort(key = lambda x : x[1])
        for duration,deadline in courses:
            heapq.heappush(heap,-duration)
            curr += duration
            if curr>deadline:
                curr -= -heapq.heappop(heap)
        return len(heap)