class Solution:
    """
        #reservoirsample #algorithm
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = idx = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            if (random.randrange(0, cnt+1) == cnt):
                idx = i
            cnt += 1
        return idx