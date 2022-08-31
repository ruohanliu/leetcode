class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            #monostack
        """
        n = len(nums)
        nextSmaller = [-1] * n
        nextBigger = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nextSmaller[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] < nums[i]:
                nextBigger[stack.pop()] = i
            stack.append(i)
        
        lo = 1
        for i in range(n):
            if nextSmaller[i]>=0:
                lo = i
                break
        hi = 0
        for i in reversed(range(n)):
            if nextBigger[i]>=0:
                hi = i
                break
        return hi-lo+1
        
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            space O(1)
        """
        n = len(nums)
        minNum = float("inf")
        started = False
        for i in range(n):
            if not started and i < n-1 and nums[i] > nums[i+1]:
                started = True
            if started:
                minNum = min(minNum,nums[i])

        maxNum = float("-inf")
        started = False
        for i in reversed(range(n)):
            if not started and i > 0 and nums[i-1] > nums[i]:
                started = True
            if started:
                maxNum = max(maxNum,nums[i])

        lo = 1
        for i in range(n):
            if nums[i] > minNum:
                lo = i
                break
        hi = 0
        for i in reversed(range(n)):
            if nums[i] < maxNum:
                hi = i
                break
        return hi-lo+1
