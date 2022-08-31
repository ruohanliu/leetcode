class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            #deque #slidingwindow
            related 862 1425

            O(n)
        """
        queue = deque()
        ans = []
        for i,x in enumerate(nums):
            while queue and nums[queue[-1]]<=x:
                queue.pop()

            queue.append(i)
            if queue[0]==i-k:
                queue.popleft()

            if i >= k-1:
                ans.append(nums[queue[0]])
        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            #heap
            O(nlogn)
        """
        heap = []
        ans = []
        for i,x in enumerate(nums):
            heapq.heappush(heap,(-x,i))

            if i >= k-1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans