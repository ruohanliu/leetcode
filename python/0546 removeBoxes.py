
class Solution:
    def removeBoxes_tle(self, boxes: List[int]) -> int:
        """
            #dp #multistate #relation #important
        """
        @cache
        def dp(l,r,k):
            if l > r:
                return 0
            while r > l and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            ans = dp(l,r-1,0) + (k+1) ** 2
            for i in range(l,r):
                if boxes[i] == boxes[r]:
                    ans = max(ans,dp(l,i,k+1)+dp(i+1,r-1,0))
            return ans

        n = len(boxes)
        return dp(0,n-1,0)

    def removeBoxes_tle(self, boxes: List[int]) -> int:
        from sortedcontainers import SortedList
        def dp(sl):
            n = len(sl)
            if n == 1:
                return sl[0][2]**2
            key = str(sl)
            if key in memo:
                return memo[key]
            ans = 0
            for i in range(n):
                index,color,cnt = sl.pop(i)
                added = None
                removed = None
                if 0<i<n-1:
                    _index,_color,_cnt = sl[i-1]
                    index_,color_,cnt_ = sl[i]
                    if _color == color_:
                        removed = [(_index,_color,_cnt),(index_,color_,cnt_)]
                        added = (_index,_color,_cnt+cnt_)
                        sl.pop(i)
                        sl.pop(i-1)
                        sl.add(added)

                ans = max(ans,cnt*cnt + dp(sl))
                if added:
                    sl.remove(added)
                    sl.add(removed[0])
                    sl.add(removed[1])
                sl.add((index,color,cnt))
            memo[key] = ans
            return ans

        memo = {}
        sl = SortedList()

        color = None
        index = None    
        for i,box in enumerate(boxes):
            if box != color:
                if color != None:
                    sl.add((index,color,cnt))
                color = box
                cnt = 1
                index = i
            else:
                cnt += 1
        sl.add((index,color,cnt))
        
        return dp(sl)