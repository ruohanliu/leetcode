class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
            #counter
        """
        dp = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        count = sum([Counter(set(combinations(dp[u], 3))) for u in dp], Counter())
        return min(count, key=lambda k: (-count[k], k))