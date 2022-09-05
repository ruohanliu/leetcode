class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
            #prefixsum #dp

            related: 325 560
        """
        n = len(arr)
        ans = float("inf")
        dp = [float("inf")]*n
        ps = 0
        i = 0
        for j,x in enumerate(arr):
            ps += x
            while ps > target:
                ps-=arr[i]
                i+=1
            if ps == target:
                ans = min(ans,j-i+1 + dp[i-1])
                dp[j] = min(dp[j-1],j-i+1)
            else:
                dp[j] = dp[j-1]
        return ans if ans < float("inf") else -1