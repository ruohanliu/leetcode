class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """
            #heap
        """
        n = len(arr)
        heap = [(arr[0] / arr[j],0,j) for j in reversed(range(1,n))]
        for _ in range(k-1):
            frc,i,j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap,(arr[i+1]/arr[j],i+1,j))
        return [arr[heap[0][1]],arr[heap[0][2]]]