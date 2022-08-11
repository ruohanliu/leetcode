class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
            #sort #optimize #binarysearch #sortedlist
        """
        from sortedcontainers import SortedList
                       
        n = len(rooms)
        m = len(queries)
        ans = [-1] * m 
        rooms.sort(key = lambda x: -x[1])
        q = sorted([(i,p,s) for i,(p,s) in enumerate(queries)],key = lambda x:-x[2])
        sl = SortedList()

        i = 0
        for k,p,s in q:
            while i < n and rooms[i][1] >= s:
                sl.add(rooms[i][0])
                i += 1
            if sl:
                j = sl.bisect_left(p)
                if j == len(sl):
                    ans[k] = sl[-1]
                elif j == 0:
                    ans[k] = sl[0]
                else:
                    ans[k] = sl[j] if abs(p-sl[j]) < abs(p-sl[j-1]) else sl[j-1]
        return ans