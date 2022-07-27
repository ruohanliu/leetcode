from collections import deque,Counter
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """
            #heap #greedy #important
            related 0378 kthSmallest

            earilest deadline first (EDF) algorithm
        """
        c = Counter(s)
        heap = [(-c[x],x) for x in c]
        heapq.heapify(heap)
        ans = []
        queue = deque()
        while heap:
            freq,char = heapq.heappop(heap)
            ans.append(char)

            queue.append((freq+1,char))
            if len(queue)>=k:
                freq,char = queue.popleft()
                if freq < 0:
                    heapq.heappush(heap,(freq,char))
        return "".join(ans) if len(s) == len(ans) else ""