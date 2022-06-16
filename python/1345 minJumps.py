from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
            #bfs #important
            Bidirectional BFS
            In the later part of our original BFS method, the layer may be long and takes a long time to compute the next layer.
            In this situation, we can compute the layer from the end, which may be short and takes less time.
        """
        from collections import defaultdict
        n = len(arr)
        ans = 0
        # index
        bfs = [0]
        # value
        visited = set()
        # value : index list
        indexMap = defaultdict(list)
        for i,num in enumerate(arr):
            indexMap[num].append(i)

        while bfs:
            bfs_next = []
            for curr in bfs:
                if curr == n-1:
                    return ans

                if arr[curr] not in visited:
                    for i in indexMap[arr[curr]]:
                        if i != curr:
                            bfs_next.append(i)
                visited.add(arr[curr])
                if curr - 1 >= 0 and arr[curr - 1] not in visited:
                    bfs_next.append(curr-1)
                if curr + 1 < n and arr[curr + 1] not in visited:
                    bfs_next.append(curr+1)
            bfs = bfs_next
            ans += 1
        return -1