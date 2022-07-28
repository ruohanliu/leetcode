class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
            #unionfind
        """
        def find(v):
            _v = v
            while v != ds[v]:
                v = ds[v]
            while _v != v:
                _v,ds[_v] = ds[_v],v
            return v
        def union(u,v):
            u = find(u)
            v = find(v)
            if u == v:
                return False
            else:
                if size[u] > size[v]:
                    size[u] += size[v]
                    ds[v] = u
                else:
                    size[v] += size[u]
                    ds[u] = v
                return True
        
        n = len(s)
        ds = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        componentChar = defaultdict(list)
        for a,b in pairs:
            union(a,b)
            
        for i in range(n):
            v = find(i)
            componentChar[v].append(s[i])
        for v in componentChar:
            componentChar[v].sort(reverse=True)
        
        ans = list(s)
        for i in range(n):
            v = find(i)
            ans[i] = componentChar[v].pop()
        return "".join(ans)
                
        