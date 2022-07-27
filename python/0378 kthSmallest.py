class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
            #heap #kth #binarysearch
        """
        m = len(matrix)
        n = len(matrix[0])
        
        heap = [(matrix[r][0],r,0) for r in range(m)]
        heapq.heapify(heap)
        while k:
            item,r,c = heapq.heappop(heap)
            if c < n - 1:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
            k -=1
        return item