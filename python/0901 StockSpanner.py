class StockSpanner:
    """
        #monostack #amortization #important
    """
    def __init__(self):
        self.monoStack = []

    def next(self, price: int) -> int:
        res = 1
        while self.monoStack and self.monoStack[-1][0] <= price:
            res += self.monoStack.pop()[1]
        self.monoStack.append((price, res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
