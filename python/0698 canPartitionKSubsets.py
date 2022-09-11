class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            #dfs #dp #bitmask #important
            related 416
            O(n*2^n)
        """
        @cache
        def dfs(state,t,completed):
            if completed == k-1:
                return True
            if t < 0:
                return False
            if t == 0:
                return dfs(state,target,completed+1)
            
            return any(dfs(state + (1<<i),t-nums[i],completed) for i in range(n) if (state>>i) % 2 == 0)

        n = len(nums)
        total = sum(nums)
        if total % k or k > n:
            return False
        target = total // k
        nums.sort(reverse=True)
        
        return dfs(0,target,0)