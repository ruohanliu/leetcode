class Solution:
    def constrainedSubsetSum_tle(self, nums: List[int], k: int) -> int:
        """
            #dp #optimize #important #deque
            related 239 862

            use deque/heap to get the max number in a window of size k
        """
        @cache
        def dp(i,started):
            if i >= n:
                return 0
            ans = max(dp(i+1,False) if not started else float("-inf"),nums[i])
            for j in range(i+1,i+k+1):
                ans = max(ans,nums[i] + dp(j,True))
            return ans
            
        n = len(nums)
        check = max(nums)
        if check < 0:
            return check
        return dp(0,False)

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
            can further reduce dp size from n to k
        """
        # dp[i] is the result for the prefix of array ending at i
        dp = nums[:]
        decQueue = deque()
        for i in range(len(nums)):
            if decQueue:
                # decQueue[0] is the max of k previous dp, only positive are kept
                dp[i] += decQueue[0]

            # must use < because dp[i-k] == decQueue[0] is used to pop out of range queue element
            while decQueue and decQueue[-1] < dp[i]:
                decQueue.pop()
            if dp[i] > 0:
                decQueue.append(dp[i])
            
            if i >= k:
                if decQueue and dp[i-k] == decQueue[0]:
                    decQueue.popleft()
        return max(dp)

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
            space optimized
        """
        decQueue = deque()
        for i in range(len(nums)):
            if decQueue:
                # decQueue[0] is the max of k previous dp, only positive are kept
                nums[i] += decQueue[0]

            # must use < because dp[i-k] == decQueue[0] is used to pop out of range queue element
            while decQueue and decQueue[-1] < nums[i]:
                decQueue.pop()
            if nums[i] > 0:
                decQueue.append(nums[i])
            
            if i >= k:
                if decQueue and nums[i-k] == decQueue[0]:
                    decQueue.popleft()
        return max(nums)

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
            store index in deque, easier to understand
        """
        decQueue = deque()
        for i in range(len(nums)):
            if decQueue:
                # decQueue[0] is the max of k previous dp, only positive are kept
                nums[i] += decQueue[0][0]

            # can use <= because index is stored in deque
            while decQueue and decQueue[-1][0] <= nums[i]:
                decQueue.pop()
            if nums[i] > 0:
                decQueue.append((nums[i],i))
            
            if i >= k and decQueue and i-k == decQueue[0][1]:
                decQueue.popleft()
        return max(nums)