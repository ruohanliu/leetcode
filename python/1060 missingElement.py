class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
            #binarysearch
            nums[i] - nums[0] - i
        """
        n = len(nums)
        if k > nums[-1] - nums[0] - n + 1:
            return k + nums[0] + n - 1
        lo = 1
        hi = n-1
        while lo < hi:
            mid = (lo+hi) // 2
            
            if nums[mid] - nums[0] - mid < k:
                lo = mid + 1
            else:
                hi = mid
        return k - (- nums[0] - lo + 1)