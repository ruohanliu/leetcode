class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        curr = 0
        for coin in coins:
            if coin - 1 > curr:
                break
            curr = curr + coin
        return curr+1
