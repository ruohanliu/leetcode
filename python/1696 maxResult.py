from typing import List
from collections import heapq,deque
class Solution:
    def maxResult_heap(self, nums: List[int], k: int) -> int:
        """
            #dp #deque #heap #important

            simple dp is too slow
            Given i, we have to find the max score between [i-k,i)
            use monotonically decreasing queue or priority queue
        """
        # dp[i] denotes the max score at i
        n = len(nums)
        dp = nums[0]
        heap = [(-nums[0],0)]
        for i in range(1,n):
            # while index not in range
            while heap[0][1] < i-k:
                heapq.heappop(heap)
            dp = -heap[0][0] + nums[i]
            heapq.heappush(heap,(-dp,i))
        return dp

    def maxResult_deque(self,nums:List[int],k:int) -> int:
        n = len(nums)
        dp = nums[0]
        monoDeque = deque([(0, dp)])
        for i in range(1, n):
            while monoDeque[0][0] < i - k:
                monoDeque.popleft()
            dp = monoDeque[0][1] + nums[i]
            while monoDeque and dp >= monoDeque[-1][1]:
                monoDeque.pop()
            monoDeque.append((i, dp))
        return dp
