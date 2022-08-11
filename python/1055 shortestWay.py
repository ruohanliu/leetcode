class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
            O(mn)
        """
        ans = 0
        n = len(target)
        j = 0
        while j < n:
            k = j
            for s in source:
                if s == target[k]:
                    k += 1
                    if k == n:
                        break
            if j == k:
                return -1
            else:
                j = k
                ans += 1
        return ans


    def shortestWay(self, source: str, target: str) -> int:
        """
            O(m + nlogm)
        """
        sourceMap = defaultdict(list)
        for i,s in enumerate(source):
            sourceMap[s].append(i)
        
        ans = 0
        srcIdx = 0
        for t in target:
            if t not in sourceMap:
                return -1
            mapIdx = bisect.bisect_left(sourceMap[t],srcIdx)
            if mapIdx == len(sourceMap[t]):
                ans += 1
                mapIdx = 0
            srcIdx = sourceMap[t][mapIdx] + 1
        return ans if srcIdx == 0 else ans + 1

    def shortestWay(self, source: str, target: str) -> int:
        """
            #greedy #important
            O(m+n)
        """
        m = len(source)
        # sourceMap[i][c] stores the earliest index of c in source >=i
        sourceMap = [[-1] * 26 for _ in range(m)]
        sourceMap[m-1][ord(source[m-1]) - ord("a")] = m-1

        for i in reversed(range(m-1)):
            sourceMap[i] = sourceMap[i+1][:]
            sourceMap[i][ord(source[i]) - ord("a")] = i

        ans = 0
        srcIdx = 0
        for t in target:
            c = ord(t) - ord("a")
            if sourceMap[0][c] == -1:
                return -1
            if sourceMap[srcIdx][c] == -1:
                ans += 1
                srcIdx = 0
            srcIdx = sourceMap[srcIdx][c] + 1
            if srcIdx == m:
                ans += 1
                srcIdx = 0

        return ans + (1 if srcIdx != 0 else 0)