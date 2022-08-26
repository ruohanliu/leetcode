class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
            #heap
        """
        n = len(nums)
        mx = float("-inf")
        dist = float("inf")
        heap = []
        for i in range(n):
            heap.append((nums[i][0],i,0))
            mx = max(mx,nums[i][0])
        heapq.heapify(heap)

        while len(heap) == n:
            mn = heap[0][0]
            if mx - mn < dist:
                dist = mx-mn
                ans = [mn,mx]
            _,r,c = heapq.heappop(heap)
            if c < len(nums[r])-1:
                heapq.heappush(heap,(nums[r][c+1],r,c+1))
                mx = max(mx,nums[r][c+1])
        return ans