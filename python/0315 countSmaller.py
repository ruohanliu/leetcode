class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
            #sortedlist #mergesort #segmenttree #fenwicktree #furtherstudy


            https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/
        """
        from sortedcontainers import SortedList
        output = [0] * len(nums)
        nums_sorted = SortedList(nums)
        for i in range(len(nums)):
            output[i] = nums_sorted.bisect_left(nums[i])
            nums_sorted.pop(output[i])
        return output