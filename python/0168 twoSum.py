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
                lo += 1
            elif numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                return [lo+1,hi+1]

        return []

        