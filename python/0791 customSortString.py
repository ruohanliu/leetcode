class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
            #customsort
        """
        rank = defaultdict(int)
        for i,x in enumerate(order):
            rank[x] = i
        def cmp(x,y):
            if rank[x]<rank[y]:
                return -1
            elif rank[x]>rank[y]:
                return 1
            else:
                return 0
        return "".join(sorted(s,key=functools.cmp_to_key(cmp)))