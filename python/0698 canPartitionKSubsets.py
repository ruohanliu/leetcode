class Solution:
    def canPartitionKSubsets_tle(self, nums: List[int], k: int) -> bool:
        """
            #backtrack #dfs #dp #bitmask #important
            O(n*2^n)
            related 416
        """
        def backtrack(i,cache):
            if i == n:
                return True
            key = tuple(tuple(cache[j]) for j in range(k))
            if key in memo:
                return False
            for j in range(k):
                if target[j] >= nums[i]:
                    target[j] -= nums[i]
                    cache[j].append(nums[i])
                    res = backtrack(i+1,cache)
                    cache[j].pop()
                    target[j] += nums[i]
                    if res:
                        return True
            memo[key] = False
            return memo[key]

        n = len(nums)
        total = sum(nums)
        if total % k or k > n:
            return False
        memo = {}
        nums.sort(reverse=True)
        cache = [[] for _ in range(k)]
        target = [total // k] * k

        return backtrack(0,cache)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            O(k*2^n)
        """
        def backtrack(i,curr,completed):
            nonlocal used
            if completed == k-1:
                return True
            if curr > target:
                return False
            if used in memo:
                return False
            if curr == target:
                return backtrack(0,0,completed+1)
            
            for j in range(i,n):
                if 1<<j & used == 0:
                    used ^= 1<<j
                    res = backtrack(i+1,curr+nums[j],completed)
                    used ^= 1<<j
                    if res:
                        return True
            
            memo.add(used)
            return False

        n = len(nums)
        total = sum(nums)
        if total % k or k > n:
            return False
        target = total // k
        nums.sort(reverse=True)
        memo = set()
        used = 0
        
        return backtrack(0,0,0)