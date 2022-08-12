class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
            #inplace
        """
        n = len(nums)
        
        one = False
        for i in range(n):
            if nums[i] == 1:
                one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not one:
            return 1
        
        for i in range(n):
            x = abs(nums[i])
            if n>= x > 0:
                nums[x-1] = - abs(nums[x-1])
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
        
                