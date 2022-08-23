class ExamRoom:
    """
        #heap
    """
    def __init__(self, n: int):
        self.seated = []
        self.n = n
    def seat(self) -> int:
        n,seated = self.n,self.seated
        if seated:
            maxDist = seated[0]
            ans = 0
            for i in range(len(seated)-1):
                if (seated[i+1] - seated[i]) // 2 > maxDist:
                    maxDist = (seated[i+1] - seated[i]) // 2
                    ans = (seated[i+1] + seated[i]) // 2
            if n-1-seated[-1] > maxDist:
                ans = n-1
        else:
            ans = 0
        bisect.insort(seated,ans)
        return ans

    def leave(self, p: int) -> None:
        self.seated.pop(bisect.bisect_left(self.seated,p))
        
    def dist(self, x, y):  # length of the interval (x, y)
        if x == -1:        # note here we negate the value to make it maxheap
            return -y
        elif y == self.N:
            return -(self.N - 1 - x)
        else:
            return -(y-x)//2
        
    def __init__(self, N):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]  # initialize heap
        
    def seat(self):
        _, x, y = heapq.heappop(self.pq)  # current max interval 
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N - 1
        else:
            seat = (x+y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))  # push two intervals by breaking at seat
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat
        
    def leave(self, p):
        head = tail = None
        for interval in self.pq:  # interval is in the form of (d, x, y)
            if interval[1] == p:  
                tail = interval
            if interval[2] == p:  
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)  # important! re-heapify after deletion
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))