from functools import reduce,accumulate
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
            #dp #relation #reduce #furtherstudy
        """
        @cache
        def game(i):
            if i == n-1:
                return ps[-1]
            return max(game(i+1),ps[i+1]-game(i+1))
        n = len(stones)
        ps = list(accumulate([0]+stones))
        return game(1)

    def stoneGameVIII_tle(self, stones: List[int]) -> int:
        return reduce(lambda memo, cur : max(memo, cur - memo), list(accumulate(stones))[::-1][:-1])