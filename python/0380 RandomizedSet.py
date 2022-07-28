class RandomizedSet:
    """
        #design
    """

    def __init__(self):
        import random
        self.val_index = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        n = len(self.arr)
        self.arr.append(val)
        self.val_index[val] = n
        return True

    def remove(self, val: int) -> bool:
        if val in self.val_index:
            i = self.val_index[val]
            n = len(self.arr)
            self.arr[n-1],self.arr[i] = self.arr[i],self.arr[n-1]
            # must update index before pop, in case there is only one element left
            self.val_index[self.arr[i]] = i
            self.arr.pop()
            del self.val_index[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return self.arr[random.randrange(0,len(self.arr))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()