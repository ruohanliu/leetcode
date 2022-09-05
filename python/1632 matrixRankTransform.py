class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """
            #unionfind #important #matrix
        """
        def find(v):
            _v = v
            while v != uf[v]:
                v = uf[v]
            while _v != v:
                _v,uf[_v] = uf[_v],v
            return v

        m = len(matrix)
        n = len(matrix[0])

        # there are m+n component, whose rank update independently
        rank = [0] * (m+n)
        items = defaultdict(list)
        for i,j in product(range(m),range(n)):
            items[matrix[i][j]].append((i,j))
        
        for val in sorted(items):
            prev = rank[:]
            # for every value, uf starts with m+n components, for each cell with the value, its row and col components are unioned
            # the cell's new rank is the larger of its prev row and col rank
            uf = list(range(m+n))
            size = [1] * (m+n)
            for i,j in items[val]:
                i = find(i)
                j = find(j+m)
                if size[i] > size[j]:
                    size[i]+=size[j]
                    uf[j] = i
                    prev[i] = max(prev[i],prev[j])
                else:
                    size[j]+=size[i]
                    uf[i] = j
                    prev[j] = max(prev[i],prev[j])
            # update rank and ans
            for i,j in items[val]:
                rank[i] = rank[j+m] = matrix[i][j] = prev[find(i)] + 1
        return matrix