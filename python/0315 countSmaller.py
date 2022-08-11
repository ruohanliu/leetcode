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

    def countSmaller(self, nums: List[int]) -> List[int]:
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]