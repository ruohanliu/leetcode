from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Longest Common Sub sequence (LIS)
        
        For a new (larger) element to be a member of an exist subset, it must be divisible by 
        the largest element in the existing subset

        nums is sorted ascendingly

        sets[num] represents the subset whose largest element is num. It is constructed by 
        selecting the largest existing subsets whose largest element can divide num, and attach num to it.

        Time and Space: N^2

        Take away:
            1. max(List/Tuple/Dict,key=len) returns the element with max size
            2. max([],key=len) is illegal
        """
        sets = {}
        for num in sorted(nums):
            candidates = [set()]
            for key in sets:
                if num % key == 0:
                    candidates.append(sets[key])
            sets[num] = max(candidates,key=len) | {num}

        return list(max(sets.values(),key=len))

    def largestDivisibleSubset_memo(self, nums: List[int]) -> List[int]:
        """
        Recursion with Memoization

        Time and Space: N^2
        """
        def wrapper(i):
            if i in memo:
                return memo[i]

            maxSubset = []
            for j in range(i):
                if nums[i] % nums[j] ==0:
                    subset = wrapper(j)
                    if len(subset) > len(maxSubset):
                        maxSubset = subset

            memo[i] = maxSubset.copy()
            memo[i].append(nums[i])
            return memo[i]

        memo = {}
        nums.sort()
        return max([wrapper(i) for i in range(len(nums))],key=len)

s = Solution()
print(s.largestDivisibleSubset_memo([1,2,3]))