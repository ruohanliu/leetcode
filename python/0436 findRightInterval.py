
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sortedIntervals = sorted((a,i) for i,(a,_) in enumerate(intervals))
        ans = [-1] * n
        for i,(_,b) in enumerate(intervals):
            j = bisect.bisect_left(sortedIntervals,(b,0))
            if j < n:
                ans[i] = sortedIntervals[j][1]
        return ans

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        heap = []
        for i,(a,b) in enumerate(sorted(intervals)):
            heapq.heappush(heap,(b,i))
            while heap and a >= heap[0][0]:
                _,j = heapq.heappop(heap)
                ans[j] = i
        return ans