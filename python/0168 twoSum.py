from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers is sorted
        """
        lo = 0
        hi = len(numbers) - 1

        while lo<hi:
            if numbers[lo] + numbers[hi] < target:
                while lo < hi and numbers[lo+1] == numbers[lo]:
                    lo += 1
                lo += 1
            elif numbers[lo] + numbers[hi] > target:
                while lo < hi and numbers[hi-1] == numbers[hi]:
                    hi -= 1
                hi -= 1
            else:
                return [lo+1,hi+1]

        return []