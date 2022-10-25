class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
            #lis
        """
        ans = 0
        n = len(scores)
        # dp[i] means the max score for a team with player[i]
        dp = [0] * n
        age_score = sorted((a,s) for s,a in zip(scores,ages))
        for j,(a,s) in enumerate(age_score):
            dp[j] = s
            for i in range(j):
                if s >= age_score[i][1]:
                    dp[j] = max(dp[j],dp[i] + s)
            
            ans = max(ans,dp[j])
        return ans