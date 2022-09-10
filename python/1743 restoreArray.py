class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
            #databricks
        """
        adjList = defaultdict(list)
        degree = defaultdict(lambda:2)
        for a,b in adjacentPairs:
            adjList[a] += b,
            adjList[b] += a,
            degree[a] -=1
            degree[b] -=1
            if degree[a] == 0:
                del degree[a]
            if degree[b] == 0:
                del degree[b]
        a,_ = degree.popitem()
        ans = []
        prev = None
        while a != None:
            ans.append(a)
            nxt = None
            for b in adjList[a]:
                if b != prev:
                    nxt = b
            prev = a
            a = nxt
        return ans