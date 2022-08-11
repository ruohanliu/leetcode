from itertools import accumulate


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            #binarysearch
        """
        def test(avg):
            sum_so_far = 0
            for i in range(k):
                sum_so_far += nums[i] - mid
            if sum_so_far >= 0:
                return True
            prev, min_so_far = 0.0, 0.0
            for i in range(k, n):
                sum_so_far += nums[i] - mid
                prev += nums[i-k]-mid
                min_so_far = min(min_so_far, prev)
                if sum_so_far >= min_so_far:
                    return True
            return False
    
        n = len(nums)
        lo, hi = min(nums), max(nums)
        precision = 1E-5
        while hi-lo > precision:
            mid = (lo+hi) / 2.0
            if test(mid):
                lo = mid
            else:
                hi = mid
        return lo