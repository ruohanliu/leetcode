class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
            #sortedlist #segmenttree #fenwicktree
            https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/
            
            related 2179
        """
        from sortedcontainers import SortedList
        sl = SortedList()
        n = len(nums)
        ans = [0] * n
        for i in reversed(range(n)):
            j = sl.bisect_left(nums[i])
            ans[i] = j
            sl.add(nums[i])
        return ans

    def countSmaller(self, nums: List[int]) -> List[int]:
        def add(i,delta):
            i = i + 1
            while i < n+1:
                bit[i] += delta
                i += i&-i

        def query(i):
            res = 0
            i = i + 1
            while i:
                res += bit[i]
                i -= i&-i
            return res

        n = len(nums)
        bit = [0] * (n+1)
        ans = [0] * n
        idxInSorted = {x: i for i, x in enumerate(sorted(nums))}
        for i in reversed(range(n)):
            rank = idxInSorted[nums[i]]
            ans[i] = query(rank-1)
            add(rank,1)
        return ans