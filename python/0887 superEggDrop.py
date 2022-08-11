class Solution:
    def superEggDrop_tle(self, k: int, n: int) -> int:
        @cache
        def dp(k,n):
            if k == 1:
                return n
            if n == 0:
                return 0
            return 1 + min(max(dp(k-1,x-1),dp(k,n-x)) for x in range(1,n+1))
        return dp(k,n)

    def superEggDrop(self, k: int, n: int) -> int:
        """
            #dp #binarysearch #important

            O(knlogn)
        """
        @cache
        def dp(k,n):
            if k == 1:
                return n
            if n == 0:
                return 0
            lo = 1
            hi = n
            while lo + 1 < hi:
                mid = (lo+hi) // 2
                if dp(k-1,mid-1) < dp(k,n-mid):
                    lo = mid
                elif dp(k-1,mid-1) > dp(k,n-mid):
                    hi = mid
                else:
                    lo = hi = mid

            return 1 + min(max(dp(k-1,x-1),dp(k,n-x)) for x in range(lo,hi+1))
        return dp(k,n)

    def superEggDrop(self, k: int, n: int) -> int:
        """
            O(klogn)
        """
        # dp[i][j] denotes the number of floors can be checked with i moves and j eggs
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                # egg breaks and doesnt break
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            if dp[i][k] >= n:
                return i

    def superEggDrop(self, k: int, n: int) -> int:
        """
            #optimize
        """
        prev = [0]*(k+1)
        curr = prev[:]
        for i in range(1,n+1):
            for j in range(1,k+1):
                curr[j] = prev[j-1] + prev[j] + 1
            if curr[-1] >= n:
                return i
            prev,curr = curr,prev