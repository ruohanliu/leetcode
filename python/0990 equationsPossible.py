class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
            #unionfind #graph
        """
        def find(a):
            _a = a
            while a != uf[a]:
                a = uf[a]
            while _a != a:
                _a,uf[_a] = uf[_a],a
            return a 

        def union(a,b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                rank[a] += rank[b]
                uf[b] = a
            else:
                rank[b] += rank[a]
                uf[a] = b
            return True

        n = 26
        uf = list(range(n))
        rank = [1] * n

        for e in equations:
            if e[1:3] == "==":
                v = ord(e[0]) - 97
                u = ord(e[3]) - 97
                union(u,v)

        for e in equations:
            if e[1:3] == "!=":
                v = ord(e[0]) - 97
                u = ord(e[3]) - 97
                if find(v) == find(u):
                    return False

        return True