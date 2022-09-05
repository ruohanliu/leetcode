class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
            #binarylifting #imporant #lca #binarysearch
            related 1483
        """
        # record depth and create binarylifting tree
        def dfs(node, parents,depth):
            depths[node] = depth
            for bit in range(m):
                if 1<<bit <= len(parents):
                    dp[node][bit] = parents[-(1<<bit)]
            parents.append(node)
            for _node in G[node]:
                if not (len(parents) >= 2 and parents[-2] == _node):
                    dfs(_node,parents,depth+1)
            parents.pop()

        def getKthParent(node,k):
            while k:
                bit = k.bit_length() - 1
                node = dp[node][bit]
                k -= 1 << bit
            return node

        def lca(a,b):
            if depths[a]>depths[b]:
                return lca(b,a)
            b = getKthParent(b,depths[b]-depths[a])
            lo = 0
            hi = depths[a]
            while lo < hi:
                mid = (lo+hi) // 2
                aa = getKthParent(a,mid)
                bb = getKthParent(b,mid)
                if aa == bb:
                    hi = mid
                else:
                    lo = mid + 1
            return getKthParent(a,lo)

        G = defaultdict(list)
        m = n.bit_length()
        for a,b in edges:
            G[a].append(b)
            G[b].append(a)
        depths = [0]*n
        dp = [[-1]*m for _ in range(n)]
        dfs(0,[],0)
        return [max([lca(a,b),lca(a,q),lca(b,q)],key=lambda x:depths[x]) for a,b,q in query]

    def closestNode_tle(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def dfs(u,path):
            if path[-1] == u:
                return set(path)
            for v in adjList[path[-1]]:
                if v != path[-2]:
                    path.append(v)
                    res = dfs(u,path)
                    path.pop()
                    if res:
                        return res
            return None
                
        def bfs(v,pathNodes):
            queue = deque([v])
            visited = set([v])
            while queue:
                v = queue.popleft()
                if v in pathNodes:
                    return v
                for _v in adjList[v]:
                    if _v not in visited:
                        visited.add(_v)
                    queue.append(_v)

        adjList = defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        ans = []
        for v,u,node in query:
            ans.append(bfs(node,dfs(u,[-1,v])))
        return ans