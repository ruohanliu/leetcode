class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
            #dp
        """
        events = sorted(zip(startTime,endTime,profit),key = lambda x:x[0])
        n = len(events)
        @cache
        def dp(i):
            if i == n:
                return 0
            j = bisect.bisect_left(events,(events[i][1],0,0),i+1)
            return max(events[i][2]+dp(j),dp(i+1))
            
        return dp(0)