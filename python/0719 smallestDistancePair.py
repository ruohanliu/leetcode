from typing import List
class Solution:
    def smallestDistancePair_tle(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if len(heap) == k:
                    heapq.heappushpop(heap, -abs(nums[i]-nums[j]))
                else:
                    heapq.heappush(heap, -abs(nums[i]-nums[j]))

        return -heap[0]

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
            #binarysearch #twopointer #important
        """
        def check(distance):
            i = 0
            j = 1
            cnt = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                cnt += j-i-1
                i += 1
            return cnt >= k

        nums.sort()
        n = len(nums)
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = (lo+hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
