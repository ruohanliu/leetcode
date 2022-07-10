from typing import List
import heapq
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
            #unionfind #graph
        """
        def find(a):
            _a = a
            while a != uf[a]:
                a = uf[a]
            while _a != a:
                _a,uf[_a] = uf[_a],a
            return a 

        def union(a,b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                rank[a] += rank[b]
                uf[b] = a
            else:
                rank[b] += rank[a]
                uf[a] = b
            return True

        uf = list(range(n))
        rank = [1] * n
        heapq.heapify(logs)
        while logs and n > 1:
            t,u,v = heapq.heappop(logs)
            if union(u,v):
                n -=1
                if n == 1:
                    return t
        return -1