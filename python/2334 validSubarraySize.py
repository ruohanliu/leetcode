class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """
            #monostack
        """
        stack = []
        n = len(nums)
        for j,x in enumerate(nums):
            while stack and nums[stack[-1]] > x:
                mid = stack.pop()
                k = j - stack[-1] - 1 if stack else mid + 1
                if nums[mid] > threshold/k:
                    return k
            stack.append(j)
        while stack:
            mid = stack.pop()
            k = n - stack[-1] - 1 if stack else n
            if nums[mid] > threshold/k:
                return k
        return -1