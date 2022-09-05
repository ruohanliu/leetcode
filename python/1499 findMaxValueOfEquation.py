class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
            #deque
            yi + yj + |xi - xj| = (yi-xi) + (yj+xj) where |xi - xj| <= k
            
            we dont care about index
        """
        ans = float("-inf")
        # store(y-x,x)
        decQueue = deque()
        for x,y in points:
            while decQueue and x - decQueue[0][1] > k:
                decQueue.popleft()
            # we want to keep the previous one for current calculation
            if decQueue:
                ans = max(ans,x+y+decQueue[0][0])
            while decQueue and decQueue[-1][0] <= y-x:
                decQueue.pop()
            decQueue.append((y-x,x))
        return ans