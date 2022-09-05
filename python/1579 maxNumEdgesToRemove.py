class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
            #unionfind
        """
        def find(a,alice):
            _a = a
            while a != uf[alice][a]:
                a = uf[alice][a]
            while _a != a:
                _a,uf[alice][_a] = uf[alice][_a],a
            return a 

        def union(a,b,alice):
            a = find(a,alice)
            b = find(b,alice)
            if a == b:
                return False
            if size[alice][a] > size[alice][b]:
                size[alice][a] += size[alice][b]
                uf[alice][b] = a
            else:
                size[alice][b] += size[alice][a]
                uf[alice][a] = b
            return True

        uf = [[i for i in range(n+1)] for _ in range(2)]
        size = [[1] * (n+1) for _ in range(2)]
        cnt = [n] * 2
        ans = 0

        for i,(t,u,v) in enumerate(sorted(edges,key = lambda x:-x[0])):
            if t == 3:
                used = False
                if union(u,v,0):
                    cnt[0] -= 1
                    used = True
                    if cnt[0] == 1 and cnt[1] == 1:
                        return ans + len(edges)-i-1
                if union(u,v,1):
                    cnt[1] -= 1
                    used = True
                    if cnt[0] == 1 and cnt[1] == 1:
                        return ans + len(edges)-i-1
                if not used:
                    ans += 1
            elif t == 2:
                if union(u,v,1):
                    cnt[1] -= 1
                    if cnt[0] == 1 and cnt[1] == 1:
                        return ans + len(edges)-i-1
                else:
                    ans += 1
            else:
                if union(u,v,0):
                    cnt[0] -= 1
                    if cnt[0] == 1 and cnt[1] == 1:
                        return ans + len(edges)-i-1
                else:
                    ans += 1
        return -1