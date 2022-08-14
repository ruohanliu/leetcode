class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        """
            #interval #segmenttree #sortedlist

            cant sort because input is ordered

            related 2276 731
        """
        from sortedcontainers import SortedList
        # stores [start,end)
        sl = SortedList()
        n = len(paint)
        ans = []
        for left,right in paint:
            i = sl.bisect_left([left,right])
            painted = 0
            # because of sorting order, only need to check 1 left side but need to check multiple right side
            if i - 1 >= 0:
                x,y = sl[i-1]
                if y >= left:
                    left = min(x,left)
                    right = max(y,right)
                    painted -= y-x
                    sl.pop(i-1)
                    i-=1
            while i < len(sl):
                x,y = sl[i]
                if right < x:
                    break
                right = max(right,y)
                painted -= y-x
                sl.pop(i)
            sl.add([left,right])
            painted += right-left
            ans.append(painted)
        return ans

    def amountPainted_jumpline(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        line = [0]*50001
        ans = [0] * n
        for i,(a,b) in enumerate(paint):
            j = a
            curr = 0
            while j < b:
                if line[j]:
                    j = line[j]
                else:
                    line[j] = b
                    j+=1
                    curr +=1
            ans[i] = curr
        return ans