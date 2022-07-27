from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
            #dp #sort
        """
        n = len(pairs)
        dp = [1] * n
        pairs.sort(key=lambda x: x[0])
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
            #sort #greedy #important
            #furtherstudy

            interval scheduling problem
        """
        n = len(pairs)
        curr = float("-inf")
        ans = 0
        pairs.sort(key=lambda x: x[1])
        for x in pairs:
            if x[0] > curr:
                ans += 1
                curr = x[1]
        return ans
