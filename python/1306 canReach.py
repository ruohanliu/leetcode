from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
            #dfs
        """
        n = len(arr)
        visited = set()
        dfs = [start]
        while dfs:
            i = dfs.pop()
            if arr[i] == 0:
                return True
            visited.add(i)
            l = i - arr[i]
            r = i + arr[i]
            if l >= 0 and l not in visited:
                dfs.append(l)
            if r < n and r not in visited:
                dfs.append(r)
        return False