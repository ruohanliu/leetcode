class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
            #optimize

            related 1383
            
            given a worker, scan thru zip(difficulty,profit), select valid, return the max profit
        """
        currMax = 0
        profitMap = []
        ans = 0
        for d,p in sorted(zip(difficulty,profit),key = lambda x: (x[0],-x[1])):
            currMax = max(currMax,p)
            if not profitMap or d > profitMap[-1][0]:
                profitMap.append((d,currMax))
        for d in worker:
            i = bisect.bisect_right(profitMap,(d,inf)) - 1
            if i >= 0:
                ans += profitMap[i][1]
        return ans