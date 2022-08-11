class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """
            #dp #optimize #bitmask
        """
        @cache
        def dp(i,state):
            if state == goal:
                return 0
            if i == n:
                return float("inf")

            _state = state
            for c in stickers[i]:
                for j in range(m):
                    if _state & 1 << j == 0 and c == target[j]:
                        _state |= 1 << j
                        break
            return min(1+dp(i,_state) if _state > state else float("inf"),dp(i+1,state))

        n = len(stickers)
        m = len(target)
        goal = (1<< m) - 1
        
        ct = Counter(target)
        _stickers = []
        for i in range(n):
            st = Counter(stickers[i])
            _stickers.append(st - (st - ct))
        toRemove = set()
        for i in range(n):
            for j in range(i+1,n):
                if not (_stickers[i] - _stickers[j]):
                    toRemove.add(i)
                elif not (_stickers[j] - _stickers[i]):
                    toRemove.add(j)
                    
        stickers = ["".join(_stickers[i].elements()) for i in range(n) if i not in toRemove]
        n = len(stickers)
        
        ans = dp(0,0)
        return ans if ans < float("inf") else -1