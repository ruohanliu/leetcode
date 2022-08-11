class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
            #sortedlist #heap

            use sortedlist to prioritize dry day, use heap to prioritize next rain lake
        """
        from sortedcontainers import SortedList
        n = len(rains)
        ans = [-1] * n
        drydays = SortedList()
        fulllake = {}
        for i,x in enumerate(rains):
            if x:
                if x in fulllake:
                    j = drydays.bisect_right(fulllake[x])
                    if j < len(drydays):
                        ans[drydays[j]] = x
                        drydays.pop(j)
                    else:
                        return []
                fulllake[x] = i
            else:
                drydays.add(i)
                # val doesnt matter, it will be overwritten
                ans[i] = 1
        return ans

    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        rain_days = defaultdict(deque)
        dry_days = []
        ans = [-1] * n

        for i,x in enumerate(rains):
            rain_days[x].append(i)
        for i,x in enumerate(rains):
            if x:
                if rain_days[x] and rain_days[x][0] < i:
                    return []
                if len(rain_days[x]) > 1:
                    heapq.heappush(dry_days,rain_days[x][1])
            else:
                if dry_days:
                    ans[i] = rains[heapq.heappop(dry_days)]
                    rain_days[ans[i]].popleft()
                else:
                    ans[i] = 1
        return ans