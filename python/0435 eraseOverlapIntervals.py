class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            #interval #greedy #important
        """
        intervals.sort()
        hi = float("-inf")
        ans = 0
        for a,b in intervals:
            # non-overlap
            if a>=hi:
                hi = b
            else:
                ans += 1
                # keep new because it is shorter and has earlier end time
                if b<hi:
                    hi = b
                else:
                    continue
        return ans