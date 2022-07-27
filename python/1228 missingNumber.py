from typing import List
class Solution:
    def missingNumber_non_math(self, arr: List[int]) -> int:
        lo = arr[1] - arr[0]
        hi = arr[-1] - arr[-2]
        if abs(hi) > abs(lo):
            return (arr[-1]+arr[-2]) //2
        elif abs(lo) > abs(hi):
            return (arr[0]+arr[1]) // 2
        for i in range(2,len(arr)):
            if abs(arr[i] - arr[i-1]) > abs(lo):
                return (arr[i] + arr[i-1]) // 2
        return arr[0]

    def missingNumber(self, arr: List[int]) -> int:
        """
            #math

            corner case
                all elements are the same, covered by the math solution
        """
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)

        