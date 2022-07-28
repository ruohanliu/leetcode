class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            #dp #memo #optimization #important #Knapsack
        """
        total = sum(nums)
        if total %2 != 0 :
            return False
        subsetTotal = total //2
        
        dp = [[False]*(subsetTotal+1) for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1,len(nums)+1):
            curr = nums[i-1]
            for j in range(subsetTotal+1):
                if j<curr:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
                    if j == subsetTotal and dp[i][j]:
                        return True
        return dp[len(nums)][subsetTotal]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0 :
            return False
        subsetTotal = total //2
        
        dp = [False]*(subsetTotal+1)
        dp[0] = True
        for curr in nums:
            # It MUST start from the right. because curr canot be reused
            for j in reversed(range(curr,subsetTotal+1)):
                dp[j] |= dp[j-curr]
        return dp[subsetTotal]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0 :
            return False
        subsetTotal = total //2
        
        # sort to use largest element first
        nums.sort(reverse=True)
        dp = [False]*(subsetTotal+1)
        dp[0] = True
        for curr in nums:
            for j in reversed(range(curr,subsetTotal+1)):
                dp[j] |= dp[j-curr]
                # terminate asap
                if j == subsetTotal and dp[j]:
                    return True
        return dp[subsetTotal]

    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i,subsetSum):
            if subsetSum == 0:
                return True
            if i == len(nums) or subsetSum < 0:
                return False
            return dfs(i+1,subsetSum) or dfs(i+1,subsetSum-nums[i])
            
        total = sum(nums)
        if total %2 != 0 :
            return False
        return dfs(0,total//2)