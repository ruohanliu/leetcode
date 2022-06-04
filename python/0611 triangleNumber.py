from typing import List
class Solution:
    def triangleNumber_bisect(self, nums: List[int]) -> int:
        """
            sort then bisect_left
        """
        from bisect import bisect_right
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                ans += bisect_right(nums,nums[i]+nums[j]-1,j+1) - j - 1
        return ans

    def triangleNumber(self, nums: List[int]) -> int:
        """
            corer case, nums[i] == 0
            sort then 3 pointer
            as k is increasing as j is increasing, no need to binary search.
            linear scan of j and k once per each i
            O(n^2)
        """
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-2):
            if nums[i] > 0:
                k = i + 2
                for j in range(i+1,n-1):
                    while k < n and nums[k] < nums[i] + nums[j]:
                        k += 1
                    ans += k - (j + 1)
        return ans

s = Solution()
print(s.triangleNumber([2,2,3,4]))
        