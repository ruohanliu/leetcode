class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """
            #dp
        """
        @cache
        def dfs(city,week):
            if week == m:
                return 0
            return max(days[i][week] + dfs(i,week+1) for i,flight in enumerate(flights[city]) if flight or i == city)

        m = len(days[0])
        return dfs(0,0)