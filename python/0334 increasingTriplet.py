from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
            #lis
            special case of LIS
        """
        from bisect import bisect_left
        lis = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
                if len(lis) == 3:
                    return True
            else:
                lis[bisect_left(lis,nums[i])] = nums[i]
        return False