class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 0:
            return 0
        adjList = defaultdict(set)
        degree = defaultdict(int)
        for a,b in roads:
            adjList[a].add(b)
            adjList[b].add(a)
            degree[a]+=1
            degree[b]+=1

        max1 = 0
        max2 = -1
        qualified = defaultdict(set)
        for v in degree:
            if degree[v] >= max1:
                if max2 < max1:
                    qualified[max2].clear()
                max2 = max1
                max1 = degree[v]
                qualified[max1].add(v)
            elif degree[v] >= max2:
                if degree[v] > max2:
                    qualified[max2].clear()
                    max2 = degree[v]
                qualified[max2].add(v)
        
        if len(qualified[max1]) > 1:
            maxV = list(qualified[max1])
            m = len(maxV)
            for i in range(m-1):
                for j in range(i+1,m):
                    if maxV[i] not in adjList[maxV[j]]:
                        return max1*2
            return max1*2 - 1
        else:
            v = qualified[max1].pop()
            for u in qualified[max2]:
                if v not in adjList[u]:
                    return max1 + max2
            return max1 + max2 - 1
                    