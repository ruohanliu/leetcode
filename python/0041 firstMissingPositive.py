class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
            #inplace
        """
        n = len(nums)
        
        one = False
        # the answer must be in [1,n+1]
        # 1st pass setting out of range to 1
        for i in range(n):
            if nums[i] == 1:
                one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not one:
            return 1
        
        # 2nd pass: setting related index to negative
        for i in range(n):
            x = abs(nums[i])
            nums[x-1] = - abs(nums[x-1])
        
        # 3rd pass: any still positive number is the answer
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1