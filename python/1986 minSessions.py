class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
            #dp #bitmask

            greedy solution doesnt work
            [2,3,3,4,4,4,5,6,7,10] 12
        """
        def backtrack(i,sessions):
            nonlocal ans
            if len(sessions) >= ans:
                return
            
            if i == n:
                ans = min(ans, len(sessions))
                return
            
            # try existing sessions
            for j in range(len(sessions)):
                if sessions[j] + tasks[i] <= sessionTime:
                    sessions[j] += tasks[i]
                    backtrack(i + 1,sessions)
                    sessions[j] -= tasks[i]
            
            # try new sessions
            sessions.append(tasks[i])
            backtrack(i + 1,sessions)
            sessions.pop()
        
        n = len(tasks)
        ans = n
        backtrack(0,[])
        return ans

    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        from sortedcontainers import SortedDict
        ans = 0
        sd = SortedDict(Counter(tasks))
        
        while sd:
            ans += 1
            remain = sessionTime
            i = sd.bisect_right(remain) - 1
            while i >= 0:
                k,v = sd.peekitem(i)
                if v == 1:
                    sd.popitem(i)
                else:
                    sd[k] -= 1
                remain -= k
                i = sd.bisect_right(remain) - 1
        return ans

        
    def minSessions_tle(self, tasks: List[int], sessionTime: int) -> int:
        ans = float("inf")
        for perm in set(permutations(tasks)):
            cnt = 1
            curr = 0
            for x in perm:
                if curr + x <= sessionTime:
                    curr += x
                else:
                    cnt += 1
                    curr = x
            ans = min(ans,cnt)
        return ans