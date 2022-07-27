class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
            #dp #binarysearch
        """
        events.sort()
        n = len(events)
        maxStart = max(events[i][0] for i in range(n))
        @cache
        def dp(i,t,k):
            if i == n or k == 0 or t >= maxStart:
                return 0
            if t >= events[i][0]:
                return dp(i+1,t,k)
            else:
                return max(events[i][2]+dp(i+1,events[i][1],k-1),dp(i+1,t,k))
            
        return dp(0,0,k)

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(tuple(event) for event in events)
        n = len(events)
        @cache
        def dp(i,k):
            if i == n or k == 0:
                return 0
            j = bisect.bisect(events,(events[i][1],float("inf"),0),i+1)
            return max(events[i][2]+dp(j,k-1),dp(i+1,k))
            
        return dp(0,k)