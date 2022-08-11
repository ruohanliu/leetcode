from itertools import accumulate
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
            #dp #math #important
            related 1547
        """
        @cache
        def dp(i,j):
            if j-i+1<k:
                return 0
            res = min(dp(i,mid) + dp(mid+1,j) for mid in range(i,j,k-1))
            if (j-i) % (k-1) == 0:
                res += stones[j+1] - stones[i]
            return res

        n = len(stones)
        stones = list(accumulate([0]+stones))
        if (n-1) % (k-1):
            return -1
        return dp(0,n-1)