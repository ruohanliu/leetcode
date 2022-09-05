class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
            #simulation
        """
        nums = list(range(n))
        i = 0 
        while len(nums) > 1: 
            i = (i + k-1) % len(nums)
            nums.pop(i)
        return nums[0] + 1

    def findTheWinner(self, n: int, k: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList(range(n))
        i = 0
        k -= 1
        for l in range(n,1,-1):
            i = (i+k) % l
            sl.pop(i)
        return sl.pop()+1