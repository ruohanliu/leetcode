class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """
            #dp #bitmask #optimize
        """
        @cache
        def dp(state,leftover):
            if sum(state) == 0:
                return 0
            return max(dp(tuple(x - (1 if i == j else 0) for j,x in enumerate(state)),(leftover - i) % batchSize) for i in range(batchSize) if state[i]) + (leftover == 0)

        n = len(groups)
        groups = [x for x in groups if x % batchSize]
        ans = n - len(groups)
        
        pos = [0]*batchSize
        for g in groups:
            pos[g%batchSize] += 1

        for leftover in range(1, batchSize):
            combine = min(pos[leftover], pos[batchSize-leftover]) if 2*leftover != batchSize else pos[leftover]//2
            ans += combine
            pos[leftover] -= combine
            pos[batchSize-leftover] -= combine
 
        return dp(tuple(pos),0) + ans