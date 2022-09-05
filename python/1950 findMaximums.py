class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        """
            #deque #monostack #important #clever
        """
        dp = nums[:]
        ans = []
        n = len(nums)
        for size in range(n):
            mx = 0
            for i in range(n-size):
                curr = min(dp[i],nums[i+size])
                dp[i] = curr
                mx = max(mx,curr)
            ans.append(mx)
        return ans

    def findMaximums(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for size in range(n):
            incQueue = deque()
            mx = 0
            for i in range(n):
                if incQueue and i - incQueue[0] + 1 > size+1:
                    incQueue.popleft()
                while incQueue and nums[incQueue[-1]] >= nums[i]:
                    incQueue.pop()
                incQueue.append(i)
                if i >= size:
                    mx = max(mx,nums[incQueue[0]])
            ans.append(mx)
        return ans

    def findMaximums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        stack = []
        for i, x in enumerate(nums + [0]):
            while stack and nums[stack[-1]] >= x:
                subarray_min = nums[stack.pop()]
                # subarray in consideration [stack[-1]+1,i-1]
                size_m_1 = (i - 1) - (stack[-1]+1) + 1 - 1 if stack else i - 1
                ans[size_m_1] = max(ans[size_m_1], subarray_min)
            stack.append(i)
        
        # there may be gaps. left to right in non-increasing order
        for i in reversed(range(n-1)): 
            ans[i] = max(ans[i], ans[i+1])
        return ans