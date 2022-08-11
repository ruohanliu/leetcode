class Solution:
    def numberWays_tle(self, hats: List[List[int]]) -> int:
        """
            #dfs #dp #bitmask #topdownorder

            O(n*2^40*40)
        """
        # state stores hat
        @cache
        def dfs(i,state):
            if i == n:
                return 1
            return sum(dfs(i+1,state | 1<<j) for j in hats[i] if 1<<j & state == 0) % mod

        n = len(hats)
        mod = 10**9+7
        return dfs(0,0)

    def numberWays(self, hats: List[List[int]]) -> int:
        """
            O(40*2^n*n)
        """
        # state stores person
        @cache
        def dfs(i,state):
            if state == target:
                return 1
            if i > 40:
                return 0
            return (dfs(i+1,state) + sum(dfs(i+1,state | 1<<j) for j in people[i] if 1<<j & state == 0)) % mod

        n = len(hats)
        mod = 10**9+7
        people = defaultdict(list)
        for i,p in enumerate(hats):
            for h in p:
                people[h].append(i)
        target = (1<<n) - 1
        return dfs(1,0)