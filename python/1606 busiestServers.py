from typing import List
from sortedcontainers import SortedDict,SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
            #sorteddict
        """
        # heap stores (endtime,server)
        heap = []
        
        # usage stores # of time server is used
        usage = [0] * k

        # freeServer[i] = j, j is next free server
        freeServer = SortedDict({i:(i+1)%k for i in range(k)})
        
        for i,(time,load) in enumerate(zip(arrival,load)):
            while heap and heap[0][0]<=time:
                _,server = heapq.heappop(heap)
                freeServer[server] = None
                prev,nextt = freeServer.peekitem(freeServer.index(server)-1)
                freeServer[server],freeServer[prev] = nextt,server
            
            if len(freeServer) == 0:
                continue
            server = i % k
            if server in freeServer:
                prev,_ = freeServer.peekitem(freeServer.index(server)-1)
            else:
                prev,_ = freeServer.peekitem(freeServer.bisect_left(server)-1)
                server = freeServer[prev]
            freeServer[prev] = freeServer[server]
            del freeServer[server]
            
            usage[server]+=1
                
            heapq.heappush(heap,(time+load,server))
        
        a = max(usage)
        return [i for i,u in enumerate(usage) if u == a]

    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
            #sortedlist
        """
        from sortedcontainers import SortedList
        # heap stores (endtime,server)
        heap = []

        # usage stores # of time server is used
        usage = [0] * k

        # freeServer[i] = j, j is next free server
        freeServer = SortedList(range(k))
        
        for i,(time,load) in enumerate(zip(arrival,load)):
            while heap and heap[0][0]<=time:
                _,server = heapq.heappop(heap)
                freeServer.add(server)
            
            if freeServer:
                serverIndex = freeServer.bisect_left(i % k) % len(freeServer)
                server = freeServer.pop(serverIndex)
                usage[server] += 1
                heapq.heappush(heap,(time+load,server))
        
        a = max(usage)
        return [i for i,u in enumerate(usage) if u == a]

    def busiestServers(self, k: int, A: List[int], B: List[int]) -> List[int]:
        """
            #heap #hard #important

            fenwick tree #furtherstudy
        """
        available = list(range(k)) # already a min-heap
        busy = [] 
        res = [0] * k
        for i, a in enumerate(A):
            while busy and busy[0][0] <= a: # these are done, put them back as available
                _, x = heapq.heappop(busy)
                heapq.heappush(available, i + (x-i)%k) # invariant: min(available) is at least i, at most i+k-1
            if available: 
                j = heapq.heappop(available) % k
                heapq.heappush(busy, (a+B[i],j))
                res[j] += 1
        a = max(res)
        return [i for i in range(k) if res[i] == a]