class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
            #monostack #important

            keeping s3, which is the maximum value below the last num (from right to left)
        """
        s3 = float("-inf")
        stack = []
        for num in reversed(nums):
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False