from random import randrange
from collections import defaultdict
class RandomizedCollection:
    """
        #design

        related 380
    """

    def __init__(self):
        self.arr = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        arr,idx = self.arr,self.idx
        n = len(self.arr)
        arr.append(val)
        idx[val].add(n)
        return len(idx[val]) == 1

    def remove(self, val: int) -> bool:
        arr,idx = self.arr,self.idx
        if val not in idx:
            return False
        i = idx[val].pop()
        if not idx[val]:
            del idx[val]
        n = len(arr)-1
        if i != n:
            idx[arr[n]].remove(n)
            idx[arr[n]].add(i)
            arr[n],arr[i] = arr[i],arr[n]
        arr.pop()
        return True

    def getRandom(self) -> int:
        arr = self.arr
        return arr[randrange(0,len(arr))]
