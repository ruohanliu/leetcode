from itertools import accumulate
class NumArray:
    """
        #segmenttree #fenwicktree #rangesum #important

        A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ft = [0] * (len(nums)+1)
        for i,x in enumerate(nums):
            self.add(i+1,x)

    def __init__(self, nums: List[int]):
        """
            efficient init
        """
        n = len(nums)
        self.nums = nums
        self.bit = [0] + nums
        for i in range(1,n+1):
            parent = i+(i&-i)
            if parent < n + 1:
                self.bit[parent] += self.bit[i]

    def add(self,i,delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i&-i
            
    def update(self, index: int, val: int) -> None:
        self.add(index+1,val-self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        right = right + 1
        while right:
            res += self.ft[right]
            right -= right&(-right)
        while left:
            res -= self.ft[left]
            left -= left&(-left)
        return res

    def sumRange(self, left: int, right: int) -> int:
        """
            slightly more efficient
        """
        res = 0
        right = right + 1
        while right > left:
            res += self.ft[right]
            right -= right&(-right)
        while left > right:
            res -= self.ft[left]
            left -= left&(-left)
        return res