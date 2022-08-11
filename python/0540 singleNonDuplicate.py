class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
            #binarysearch
            O(n)
        """
        return reduce(xor,nums)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lo = 0
        hi = n-1
        while lo<=hi:
            mid = (lo+hi) // 2
            if mid+1 <= n-1 and nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    lo = mid+2
                else:
                    hi = mid-1
            elif mid > 0 and nums[mid] == nums[mid-1]:
                if mid % 2 == 0:
                    hi = mid-2
                else:
                    lo = mid+1
            else:
                return nums[mid]