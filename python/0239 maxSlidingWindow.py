class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
            #deque
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