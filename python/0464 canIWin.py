class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
            #dfs #dp
        """
        # returns if alice wins
        memo = {}
        def dfs(nums,target):
            if nums[-1] >= target:
                return True
            key = tuple(nums)
            if key in memo:
                return memo[key]
            for i,x in enumerate(nums):
                if not dfs(nums[:i]+nums[i+1:],target - x):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        total = (1+maxChoosableInteger) * maxChoosableInteger // 2
        if total < desiredTotal:
            return False
        if total == desiredTotal:
            return maxChoosableInteger % 2 == 1

        return dfs(list(range(1,maxChoosableInteger+1)),desiredTotal)