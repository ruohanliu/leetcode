from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            #unionfind #important

            Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        """

        s = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in s:
                curr = 1

                while n+1 in s:
                    n+=1
                    curr +=1
                
                ans = max(ans,curr)
        return ans