from operator import add,mul,truediv,sub
from math import isclose
class Solution:
    """
        #dfs
    """
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(cards):
            n = len(cards)
            if n == 1:
                return isclose(cards[0],24)
            return any(dfs((op(perm[0],perm[1]),)+perm[2:])
                for perm in itertools.permutations(cards)
                    for op in (add,mul,truediv,sub)
                        if not (isclose(perm[1],0) and op == truediv))
        return dfs(cards)

    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(cards):
            n = len(cards)
            if n == 1:
                return abs(cards[0] - 24) < 0.01
            for perm in itertools.permutations(cards):
                for i in range(n-1):
                    for op in (add,mul,truediv,sub):
                        if perm[i+1] == 0 and op == truediv:
                            continue
                        _cards = perm[:i] + (op(perm[i],perm[i+1]),) + perm[i+2:]
                        if dfs(_cards):
                            return True
            return False
        return dfs(cards)