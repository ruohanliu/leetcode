class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
            #heap

            minheap pops the smallest number, while fixed size minheap keeps the largest k numbers.
        """
        heap = []
        for n in nums:
            if len(heap)<k:
                heapq.heappush(heap,n)
            else:
                heapq.heappushpop(heap,n)
        
        c = Counter(heap)
        ans = []
        for n in nums:
            if c[n] > 0:
                ans.append(n)
                c[n] -=1
        return ans