class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """
            #dp
        """
        @cache
        def dp(i,j):
            if j == n:
                return 0
            ans = float("inf")
            for k in range(m):
                if ring[(i+k) % m] == key[j]:
                    ans = min(ans,k+1+dp((i+k)%m,j+1))
                    break
            for k in range(m):
                if ring[(i-k) % m] == key[j]:
                    ans = min(ans,k+1+dp((i-k)%m,j+1))
                    break
            return ans

        m = len(ring)
        n = len(key)
        return dp(0,0)