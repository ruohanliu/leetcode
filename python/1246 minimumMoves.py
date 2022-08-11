class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        """
            #dp #palindrome
        """
        @cache
        def dp(i,j):
            if i == j or (i+1 == j and arr[i] == arr[j]):
                return 1
            if i > j:
                return 0
            if arr[i] == arr[j]:
                return dp(i+1,j-1)

            ans = min(dp(i+1,j)+1,dp(i,j-1)+1,dp(i+1,j-1)+2)
            for k in range(i+1,j):
                ans = min(ans,dp(i,k)+dp(k+1,j))
            return ans
        return dp(0,len(arr)-1)