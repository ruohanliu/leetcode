from collections import defaultdict,Counter
from typing import List
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
            #important
            #furtherstudy
            keep a constant, still ensure iteration over all possible pairs
        """
        # We will take a dictionary to store the sums of nums[a] and nums[b]
        dic = defaultdict(int)
        n = len(nums)
        quadruplets_count = 0

        # we will take two constants c and b for each iteration of first for loop,
        # b would be one lesser than c
        # then we will loop from left to pickup a for summing up with our constant b
        # Similarly we will loop from right side of c to pickup d to calculate (d-c)
        for c in range(2, n-1):
            b = c-1
            for a in range(b):
                dic[nums[a] + nums[b]] += 1
            for d in range(c+1, n):
                quadruplets_count += dic[nums[d] - nums[c]]
        return quadruplets_count


    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        freq = Counter()
        n = len(nums)

        for bc in range(n):
            # bc serves as c
            for d in range(bc+1, n):
                ans += freq[nums[d] - nums[bc]]
            
            # bc serves as b
            for a in range(bc):
                freq[nums[a] + nums[bc]] += 1
        return ans
