class MajorityChecker:
    """
        #design #majority #binarysearch

        O(logn * logn)
    """
    def __init__(self, arr: List[int]):
        self.idx = defaultdict(list)
        for i,x in enumerate(arr):
            self.idx[x] += i,
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            i = random.randrange(left,right+1)
            x = self.arr[i]
            l = bisect.bisect_left(self.idx[x],left)
            r = bisect.bisect_right(self.idx[x],right)
            if r-l >= threshold:
                return x
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)