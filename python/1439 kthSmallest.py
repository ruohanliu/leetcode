class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
            #heap #dijkstra
            related 373
        """
        m = len(mat)
        n = len(mat[0])
        heap = [(sum(mat[i][0] for i in range(m)),(0,)*m)]
        visited = {(0,)*m}
        for _ in range(k):
            total, indices = heapq.heappop(heap)
            for i,j in enumerate(indices):
                if j < n-1:
                    _indices = tuple(_j+1 if _i == i else _j for _i,_j in enumerate(indices))
                    if _indices not in visited:
                        visited.add(_indices)
                        heapq.heappush(heap,(total + mat[i][j+1] - mat[i][j],_indices))
        return total