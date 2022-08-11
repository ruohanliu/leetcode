from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
            #graph #twopointer 
        """
        degree = [0] * (n+1)
        shared = defaultdict(int)
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
            shared[min(u,v),max(u,v)] += 1
        ans = []
        sortedDegree = sorted(degree)
        for q in queries:
            # incident(u,v) > q
            cnt = 0

            # count pairs sume of whose degree > q
            lo = 1
            hi = n
            while lo < hi:
                if sortedDegree[lo] + sortedDegree[hi] > q:
                    cnt += hi-lo
                    hi -= 1
                else:
                    lo += 1
            
            # minus the pairs not qualifying without their shared edges
            cnt -= sum(1 for (u,v),val in shared.items() if degree[u] + degree[v] > q and degree[u] + degree[v] - val <= q)
            ans.append(cnt)
        return ans