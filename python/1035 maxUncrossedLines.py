class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
            #dp #lcs
            related 1143 
        """
        @cache
        def dp(i,j):
            if i == n or j == m:
                return 0
            if nums1[i] == nums2[j]:
                return dp(i+1,j+1) + 1
            else:
                return max(dp(i,j+1),dp(i+1,j))

        n = len(nums1)
        m = len(nums2)
        return dp(0,0)

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        n = len(nums1)
        m = len(nums2)

        curr = [0] * (m+1)
        prev = curr[:]

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if nums1[i] == nums2[j]:
                    curr[j] = prev[j+1] + 1
                else:
                    curr[j] = max(prev[j],curr[j+1])
            curr,prev = prev,curr
        return prev[0]