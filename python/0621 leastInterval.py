class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            #queue #heap #math #important #greedy
        """
        if n == 0:
            return len(tasks)
        queue = deque()
        count = Counter(tasks)
        count = [-count[k] for k in count]
        heapq.heapify(count)
        ans = 0
        m = len(tasks)
        while m:
            ans += 1
            if count:
                m-=1
                curr = heapq.heappop(count)
                if curr<-1:
                    queue.append((curr+1,ans+n))
            while queue and queue[0][1] <= ans:
                heapq.heappush(count,queue.popleft()[0])
        return ans

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        count = Counter(tasks)
        maxFreq = max(count.values())
        maxFreqCnt = sum(1 for freq in count.values() if freq == maxFreq)
        worstCase = (maxFreq-1)*(n+1) + maxFreqCnt
        
        return max(len(tasks), worstCase)