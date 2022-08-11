class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
            #dp #bottomuporder
        """
        @cache
        def dp(fuel,i):
            if abs(locations[finish] - locations[i]) > fuel:
                return 0
            return ((1 if i == finish else 0) + sum(dp(fuel - abs(locations[i]-_pos),j) for j,_pos in enumerate(locations) if j != i)) % mod
        mod = 10**9 + 7
        return dp(fuel,start)

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        n = len(locations)
        dp = [[0]*(fuel+1) for _ in range(n)]
        dp[start][fuel] = 1
        for f in reversed(range(fuel+1)):
            for i,pos in enumerate(locations):
                if dp[i][f]:
                    for j,_pos in enumerate(locations):
                        _f = f - abs(pos-_pos)
                        if i != j and _f >= 0:
                            dp[j][_f] = (dp[i][f]+dp[j][_f]) % mod
        return sum(dp[finish]) % mod
