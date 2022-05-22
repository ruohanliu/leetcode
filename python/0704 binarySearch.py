from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(i,j):
            if i > j:
                return -1

            mid = (i+j)//2
            if target > nums[mid]:
                return binary_search(mid+1,j)
            elif target < nums[mid]:
                return binary_search(i,mid-1)
            else:
                return mid
        return binary_search(0,len(nums)-1)
        