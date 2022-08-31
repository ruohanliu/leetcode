class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
            #dp
            related 312
        """
        @cache
        def dp(i,j):
            if i+1 == j:
                return 0
            ans = float("inf")
            side = values[i]*values[j]
            for k in range(i+1,j):
                ans = min(ans,side*values[k] + dp(i,k) + dp(k,j))
            return ans
        
        return dp(0,len(values)-1)
            