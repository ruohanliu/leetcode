class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        """
            #prefixsum
        """
        n = len(beans)
        beans.sort()
        ps = list(accumulate([0]+beans))
        ans = float("inf")
        for i in range(n):
            ans = min(ans, ps[-1] - (n-i) * beans[i])
        return ans

    def minimumRemoval(self, beans: List[int]) -> int:
        return sum(beans) - max((len(beans)-i) * x for i,x in enumerate(sorted(beans)))
        
