from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        sliding window method

        take away:
            1. need clearly think about how outer loops move. It can be simplified as moving right pointer
            2. sliding window method time complexity O(n), but it does not work with negative numbers and float numbers
        """
        ans = 0
        lo = 0
        hi = 0
        p = 1
        while lo < len(nums):
            # if windows size is 0
            if lo == hi:
                hi += 1
                p *= nums[lo]
            elif p < k:
                # found a window
                ans += hi - lo
            
                if hi == len(nums): break

                if p * nums[hi] >= k:
                    p = p / nums[lo]
                    lo += 1

                p *= nums[hi]
                hi += 1
            else:
                if lo < hi:
                    p /= nums[lo]
                    lo += 1
        return ans
s = Solution()
print(s.numSubarrayProductLessThanK([1,1,1,1,1],1000))
