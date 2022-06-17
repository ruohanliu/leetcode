class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
            #monostack #dp
        """
        def maxHistogramArea(nums:List[int]) -> int:
            ans = 0
            n = len(nums)
            prevMinIndex = [-1] * n
            nextMinIndex = [n] * n
            monoStack = []
            for i in range(n):
                while monoStack and nums[monoStack[-1]] > nums[i]:
                    nextMinIndex[monoStack.pop()] = i
                monoStack.append(i)
            monoStack = []
            for i in range(n-1,-1,-1):
                while monoStack and nums[monoStack[-1]] >= nums[i]:
                    prevMinIndex[monoStack.pop()] = i
                monoStack.append(i)
            for i in range(n):
                ans = max(ans,nums[i]*(nextMinIndex[i]-prevMinIndex[i]-1))
            return ans

        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[j] = (dp[j] + 1) if matrix[i][j] == "1" else 0
            ans = max(ans,maxHistogramArea(dp))
        return ans
