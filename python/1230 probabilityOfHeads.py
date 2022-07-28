class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j] probability for i toss and j facing up
        dp = [[0] * (n+1) for _ in range(n)]
        dp[0][0] = 1-prob[0]
        dp[0][1] = prob[0]
        for i in range(1,n):
            for j in range(min(i+2,target+1)):
                dp[i][j] = (dp[i-1][j] * (1 - prob[i]) if j < i+1 else 0) + dp[i-1][j-1] * prob[i]
        return dp[-1][target]

    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
            #dp #optimized
        """
        n = len(prob)
        # dp[j] probability for j facing up
        dp = [1] + [0] * target
        for i in range(n):
            for j in reversed(range(target+1)):
                dp[j] = dp[j] * (1 - prob[i])  + (dp[j-1] if j else 0) * prob[i]
        return dp[-1]