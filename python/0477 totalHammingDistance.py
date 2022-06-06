from typing import List
class Solution:
    def totalHammingDistance_tle(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                ans += (nums[i]^nums[j]).bit_count()
        return ans

    def totalHammingDistance(self, nums: List[int]) -> int:
        """
            #important #vectorization #bitwise #hammingdistance #itertools #zip_longest

            zip_longest(*iterable,fillvalue=)
        """
        from itertools import zip_longest
        return sum([sum(pos)*(len(nums)-sum(pos)) for pos in zip_longest(*[[int(b) for b in bin(num)[2:]][::-1] for num in nums],fillvalue=0)])
s = Solution()
print(s.totalHammingDistance([5,6,42,52,666234]))