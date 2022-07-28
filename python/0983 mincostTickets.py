class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
            #dp
        """
        @cache
        def plan(d):
            if d > 365:
                return 0
            if d in day:
                return min(\
                    costs[0] + plan(d+1),\
                    costs[1] + plan(d+7),\
                    costs[2] + plan(d+30))
            else:
                return plan(d+1)

        day = set(days)
        return plan(1)