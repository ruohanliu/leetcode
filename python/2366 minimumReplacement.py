class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
            #greedy
        """
        ans = 0
        n = len(nums)
        prev = nums[-1]
        for i in reversed(range(n-1)):
            if nums[i]>prev:
                if nums[i] % prev == 0:
                    ans += nums[i] // prev - 1
                else:
                    pieces = nums[i] // prev + 1
                    ans += pieces - 1
                    prev = nums[i] // pieces
            else:
                prev = nums[i]
        return ans
