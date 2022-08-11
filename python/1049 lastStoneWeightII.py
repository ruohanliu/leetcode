class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
            #knapsack
            related 494 416
        """
        sums = {0}
        total = sum(stones)
        for x in stones:
            sums |= {x+y for y in sums}
        return min(abs(total - x - x) for x in sums)

    def lastStoneWeightII(self, stones: List[int]) -> int:
        diff = {0}
        for x in stones:
            diff = {x+y for y in diff} | {abs(x-y) for y in diff}
        return min(diff)