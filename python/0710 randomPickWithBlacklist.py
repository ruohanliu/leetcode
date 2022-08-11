class Solution:
    """
        #binarysearch #furtherstudy
    """
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.b = sorted(blacklist)

    def pick(self) -> int:
        w = random.randrange(self.n - len(self.b))
        lo = 0
        hi = len(self.b)-1
        while lo < hi:
            mid = (lo+hi) // 2 + 1
            if self.b[mid] - mid > w:
                hi = mid - 1
            else:
                lo = mid
        return w + lo + 1 if lo == hi and self.b[lo] - lo <= w else w


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()