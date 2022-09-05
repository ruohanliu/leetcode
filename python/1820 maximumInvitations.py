class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
            #hungarian #maximum_bipartite_matching #hopcroft-karp #algorithm #important
            related 1349

            O((V+E)^3)
        """
        def dfs(boy,seen):
            for girl in range(n):
                # Only ask that girl if you haven't asked her before already.
                if grid[boy][girl] and not seen[girl]:
                    seen[girl] = True
                    # if you wish to ask a girl that's taken, she will only go with you ff her current partner finds a new girl
                    if match[girl] == -1 or dfs(match[girl],seen):
                        match[girl] = boy
                        return True
            return False
        
        m, n = len(grid), len(grid[0])
        ans = 0
        match = [-1] * n
        
        for boy in range(m):
            if dfs(boy,[False] * n):
                ans += 1
        return ans

    def maximumInvitations(self, grid: List[List[int]]) -> int:
        """
            #backtrack
        """
        m, n = len(grid), len(grid[0])
        
        ans = 0
        def backtracking(i, curr):
            nonlocal ans
            if i == m:
                ans = max(ans, len(curr))
                return
            
            # try all possible invitation
            for j in range(n):
                if grid[i][j] == 1 and j not in curr:
                    curr.add(j)
                    backtracking(i+1, curr)
                    curr.discard(j)
                    
            # invite no one
            backtracking(i+1, curr)
        
        backtracking(0, set())
        return ans

    def maximumInvitations(self, grid: List[List[int]]) -> int:
        '''Find maximum cardinality matching of a bipartite graph (U,V,E).
        The input format is a dictionary mapping members of U to a list
        of their neighbors in V.  The output is a triple (M,A,B) where M is a
        dictionary mapping members of V to their matches in U, A is the part
        of the maximum independent set in U, and B is the part of the MIS in V.
        The same object may occur in both U and V, and is treated as two
        distinct vertices if this happens.'''
        
        # initialize greedy matching (redundant, but faster than full search)
        m, n = len(grid), len(grid[0])
        matching = {}
        for u in range(m):
            for v in range(n):
                if grid[u][v] and v not in matching:
                    matching[v] = u
                    break
        
        while True:
            # structure residual graph into layers
            # pred[u] gives the neighbor in the previous layer for u in U
            # preds[v] gives a list of neighbors in the previous layer for v in V
            # unmatched gives a list of unmatched vertices in final layer of V,
            # and is also used as a flag value for pred[u] when u is in the first layer
            preds = {}
            unmatched = []
            pred = dict([(u,unmatched) for u in range(m)])
            for v in matching:
                del pred[matching[v]]
            layer = list(pred)
            
            # repeatedly extend layering structure by another pair of layers
            while layer and not unmatched:
                newLayer = {}
                for u in layer:
                    for v in range(n):
                        if grid[u][v] and v not in preds:
                            newLayer.setdefault(v,[]).append(u)
                layer = []
                for v in newLayer:
                    preds[v] = newLayer[v]
                    if v in matching:
                        layer.append(matching[v])
                        pred[matching[v]] = v
                    else:
                        unmatched.append(v)
            
            # did we finish layering without finding any alternating paths?
            if not unmatched:
                unlayered = {}
                for u in range(m):
                    for v in range(n):
                        if grid[u][v] and v not in preds:
                            unlayered[v] = None
                return len(matching)

            # recursively search backward through layers to find alternating paths
            # recursion returns true if found path, false otherwise
            def recurse(v):
                if v in preds:
                    L = preds[v]
                    del preds[v]
                    for u in L:
                        if u in pred:
                            pu = pred[u]
                            del pred[u]
                            if pu is unmatched or recurse(pu):
                                matching[v] = u
                                return 1
                return 0

            for v in unmatched: recurse(v)