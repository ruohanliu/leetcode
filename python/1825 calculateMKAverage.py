class Fenwick: 
    """
        #fenwicktree
    """
    def __init__(self, n: int):
        self.bit = [0]*(n+1)

    def sum(self, i: int) -> int: 
        i += 1
        ans = 0
        while i:
            ans += self.bit[i]
            i -= i&-i
        return ans

    def add(self, i: int, delta: int) -> None: 
        i += 1
        while i < len(self.bit): 
            self.bit[i] += delta
            i += i&-i

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k 
        self.data = deque()
        self.value = Fenwick(10**5+1)
        self.index = Fenwick(10**5+1)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.index.add(num, 1)
        if len(self.data) > self.m: 
            num = self.data.popleft()
            self.value.add(num, -num)
            self.index.add(num, -1)

    def _getindex(self, k): 
        lo, hi = 0, 10**5 + 1
        while lo < hi: 
            mid = (lo + hi) // 2
            if self.index.sum(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo 
            
    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m: return -1 
        lo = self._getindex(self.k)
        hi = self._getindex(self.m-self.k)
        ans = self.value.sum(hi) - self.value.sum(lo)
        ans += (self.index.sum(lo) - self.k) * lo
        ans -= (self.index.sum(hi) - (self.m-self.k)) * hi
        return ans // (self.m - 2*self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

class MKAverage:
    """
        #heap #furtherstudy
    """
    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.arr = [0]*m
        self.lh1, self.rh1 = self.heap_init(m, k)
        self.lh2, self.rh2 = self.heap_init(m, m - k)
        self.score = 0
        
    def heap_init(self, p1, p2):
        h1 = [(0, i) for i in range(p1-p2, p1)]
        h2 = [(0, i) for i in range(p1-p2)]
        heapq.heapify(h1)
        heapq.heapify(h2)
        return (h1, h2)
        
    def update(self, lh, rh, m, k, num):
        score, T = 0, len(self.arr)
        if num > rh[0][0]:
            heappush(rh, (num, T))        
            if self.arr[T - m] <= rh[0][0]:
                if rh[0][1] >= T - m: score += rh[0][0]
                score -= self.arr[T - m]
                heappush(lh, (-rh[0][0], rh[0][1]))
                heappop(rh)
        else:
            heappush(lh, (-num, T))       
            score += num
            if self.arr[T - m] >= rh[0][0]: 
                heappush(rh, (-lh[0][0], lh[0][1]))
                q = heappop(lh)
                score += q[0]
            else:
                score -= self.arr[T - m]

        while lh and lh[0][1] <= T - m: heappop(lh)  # lazy-deletion
        while rh and rh[0][1] <= T - m: heappop(rh)  # lazy-deletion
        return score
        
    def addElement(self, num):
        t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
        t2 = self.update(self.lh2, self.rh2, self.m, self.m - self.k, num)
        self.arr.append(num)
        self.score += (t2 - t1)
    
    def calculateMKAverage(self):
        if len(self.arr) < 2*self.m: return -1
        return self.score//(self.m - 2*self.k)