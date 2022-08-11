class SnapshotArray:
    """
        #binarysearch

        bisect can be used on list of list
    """
    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [[[self.snap_id,0]] for _ in range(length)]
    def set(self, index: int, val: int) -> None:
        if not self.arr[index] or self.arr[index][-1][0] != self.snap_id:
            self.arr[index].append([self.snap_id,val])
        else:
            self.arr[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        if not self.arr[index]:
            return 0
        i = bisect.bisect_right(self.arr[index],[snap_id,inf])-1
        if i >=0:
            return self.arr[index][i][1]