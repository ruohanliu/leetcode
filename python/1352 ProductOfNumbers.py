class ProductOfNumbers:
    """
        #design #prefixproduct
    """
    def __init__(self):
        self.pp = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pp = [1]
        else:
            self.pp.append(self.pp[-1]*num)

    def getProduct(self, k: int) -> int:
        if len(self.pp) - 1 < k:
            return 0
        else:
            return self.pp[-1] // self.pp[-1-k]
