class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
            #dp
        """
        dp = defaultdict(int)
        for num in arr:
            dp[num] = max(dp[num], 1+dp[num-difference])
        return max(dp.values())

    def longestSubsequence_tle(self, arr: List[int], difference: int) -> int:
        """
            #lis
        """
        n = len(arr)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)