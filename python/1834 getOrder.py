from heapq import *
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
            #heap
            related 1882
        """
        taskQueue = []
        ans = []
        tasks = sorted([(a,b,i) for i,(a,b) in enumerate(tasks)])
        servertime = tasks[0][0]
        for enQueueTime,grp in groupby(tasks,key = lambda x:x[0]):
            while taskQueue and servertime < enQueueTime:
                processingTime,i = heappop(taskQueue)
                ans.append(i)
                servertime += processingTime
                
            servertime = max(servertime,enQueueTime)
            for _,processingTime,i in grp:
                heappush(taskQueue,(processingTime,i))
            
        while taskQueue:
            ans.append(heappop(taskQueue)[1])
        return ans