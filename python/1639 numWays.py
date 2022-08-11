class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
            #dp #bottomuporder
        """
        @cache
        def dp(k,w):
            if k == m:
                return 1
            if w == n:
                return 0
            c = target[k]
            ans = dp(k,w+1)
            if count[w,c]:
                ans += count[w,c] * dp(k+1,w+1)
            return ans % mod

        n = len(words[0])
        m = len(target)
        mod = 10 ** 9 + 7
        count = Counter()
        for word in words:
            for i,c in enumerate(word):
                count[i,c] += 1
        return dp(0,0)

    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        mod = 10 ** 9 + 7
        dp = [1] + [0] * m
        count = Counter()
        for word in words:
            for i,c in enumerate(word):
                count[i,c] += 1
        for w in range(n):
            for k in reversed(range(1,m+1)):
                dp[k] += dp[k-1] * count[w,target[k-1]] % mod

        return dp[m] % mod