from heapq import *
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
            #heap
            related 1834
        """
        servers = [(w, i) for i,w in enumerate(servers)]
        heapify(servers)
        # stores (end time, server)
        tasks_in_progress = []
        ans = []
        moment = 0
        for i,time in enumerate(tasks):
            # advance moment
            moment = max(moment, i)
            if not servers:
                moment = tasks_in_progress[0][0]
            # clear finished tasks
            while tasks_in_progress and tasks_in_progress[0][0] <= moment:
                heappush(servers, heappop(tasks_in_progress)[1])
            # assign server for current task
            ans.append(servers[0][1])
            heappush(tasks_in_progress, (moment + time, heappop(servers)))
        return ans