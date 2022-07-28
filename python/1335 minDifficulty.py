class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        @cache
        def dfs(i,d):
            if d == 1:
                return max(jobDifficulty[i:])
            ans = float("inf")
            maxDifficulty = 0
            # n-j-1<=d-1
            for j in range(i,n-d+1):
                maxDifficulty = max(maxDifficulty,jobDifficulty[j])
                ans = min(ans,maxDifficulty + dfs(j+1,d-1))
            return ans

        return dfs(0,d)


    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
            #dp
        """
        n = len(jobDifficulty)
        if d > n:
            return -1
        # dp[d][i] minDifficulty for starting i-th job on d-th day
        dp = [[float("inf")] * n for _ in range(d+1)]
        dp[d][-1] = jobDifficulty[-1]

        # On the last day, we must schedule all remaining jobs, so dp[d][i] is the maximum difficulty job remaining
        for i in reversed(range(n-1)):
            dp[d][i] = max(dp[d][i+1], jobDifficulty[i])

        for day in reversed(range(1,d)):
            # n - (i+1) >= d-day
            # on day, number of completed job is at least day, at most n-d+day
            for i in range(day-1,n-d+day):
                maxDifficulty = 0
                for j in range(i,n-d+day):
                    maxDifficulty = max(maxDifficulty,jobDifficulty[j])
                    dp[day][i] = min(dp[day][i],maxDifficulty + dp[day+1][j+1])
        return dp[1][0]

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
            #dp #optimized #monostack #important

            https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution
        """
        n = len(jobDifficulty)
        if d > n:
            return -1
        prev = [float("inf")] * n
        curr = [0] * n

        for day in range(d):
            monoStack = []
            for i in range(day,n-d+day+1):
                curr[i] = prev[i-1] + jobDifficulty[i] if i else jobDifficulty[i]
                while monoStack and jobDifficulty[monoStack[-1]] <= jobDifficulty[i]:
                    j = monoStack.pop()
                    curr[i] = min(curr[i],curr[j] - jobDifficulty[j] + jobDifficulty[i])
                if monoStack:
                    curr[i] = min(curr[i],curr[monoStack[-1]])
                monoStack.append(i)
            prev,curr = curr,prev
        return prev[-1]