class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        """
            #unionfind
        """
        def isSimilar(s,t):
            cnt = 0
            for a,b in zip(s,t):
                if a!= b:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt != 1            
        ans = 0
        strs = set(strs)
        while strs:
            queue = deque([strs.pop()])
            ans += 1
            while queue:
                for _ in range(len(queue)):
                    a = queue.popleft()
                    strs.discard(a)
                    for b in strs:
                        if isSimilar(a,b):
                            queue.append(b)
        return ans

    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s,t):
            cnt = 0
            for a,b in zip(s,t):
                if a!= b:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt != 1

        def find(v):
            _v = v
            while v != uf[v]:
                v = uf[v]
            while _v != v:
                _v,uf[_v] = uf[_v],v
            return v

        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return 0
            if size[u] > size[v]:
                size[u] += size[v]
                uf[v] = u
            else:
                size[v] += size[u]
                uf[u] = v
            return 1

        strs = list(set(strs))
        n = len(strs)
        ans = n
        uf = list(range(n))
        size = [1] * n
        for i in range(n):
            for j in range(i+1,n):
                if isSimilar(strs[i],strs[j]):
                    ans -= union(i,j)
        return ans
