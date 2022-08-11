class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
            #heap
        """
        m = len(mat)
        n = len(mat[0])
        heap = [(mat[i][0],i,0) for i in range(m)]
        heapq.heapify(heap)
        cnt = 0
        prev= None
        while heap:
            curr,r,c = heapq.heappop(heap)
            if curr == prev:
                cnt += 1
                if cnt == m:
                    return curr
            else:
                cnt = 1
                prev = curr
            if c < n-1:
                heapq.heappush(heap,(mat[r][c+1],r,c+1))
        return -1

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        intersect = reduce(operator.__and__,map(set,mat))
        return min(intersect) if intersect else -1