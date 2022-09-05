class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """
            #bfs #cycle #hard
        """
        def bfs(v,seen):
            queue = deque([v])
            ans = 0
            while queue:
                ans += 1
                for _ in range(len(queue)):
                    v = queue.popleft()
                    for _v in adjList[v]:
                        if not seen[_v]:
                            seen[_v] = True
                            queue.append(_v)
            return ans

        n = len(favorite)
        adjList = defaultdict(list)
        for i,x in enumerate(favorite):
            adjList[x].append(i)

        # Find max cycle
        maxCycle = [0] * n
        for i in range(n):
            if maxCycle[i] == 0:
                curr = i
                val = 0
                visited = {}
                while curr not in visited:
                    if maxCycle[curr]:
                        cnt = maxCycle[curr]
                        break
                    visited[curr] = val
                    val += 1
                    curr = favorite[curr]
                else:
                    cnt = val - visited[curr]
                
                for j in visited:
                    maxCycle[j] = cnt

        # find dual and their followers
        ans = 0
        seen = [False] * n
        for i,x in enumerate(favorite):
            if favorite[x] == i and not seen[i]:
                seen[x] = seen[i] = True
                ans += bfs(x,seen) + bfs(i,seen)

        return max(ans,max(maxCycle))