from bisect import bisect


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        """
            #binarysearch

            naive is O(mn). Reduce to O(nlogn + mklogk + mlogklogn)
        """
        n = len(packages)
        m = len(boxes)
        packages.sort()
        ans = float("inf")
        for i in range(m):
            boxes[i].sort()
            if boxes[i][-1] < packages[-1]:
                continue
            curr = 0
            p = 0
            b = 0
            while p < n:
                b = bisect.bisect_left(boxes[i],packages[p],b)
                prev = p
                p = bisect.bisect_right(packages,boxes[i][b],p)
                curr += boxes[i][b] * (p-prev)
            ans = min(ans,curr)
        return (ans - sum(packages)) % (10**9+7) if ans < float("inf") else -1