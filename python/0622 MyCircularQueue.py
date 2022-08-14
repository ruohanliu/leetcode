from threading import Lock
class MyCircularQueue:
    """
        #queue #lock #design
    """
    def __init__(self, k: int):
        self.queue = [0] * k
        self.start = 0
        self.end = 0
        self.full = False
        self.lock = Lock()

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            # automatically acquire the lock when entering the block
            with self.lock:
                self.queue[self.end] = value
                self.end = (self.end + 1) % len(self.queue)
                if self.start == self.end:
                    self.full = True
                return True
            # automatically release the lock when leaving the block
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            with self.lock:
                if self.start == self.end:
                    self.full = False
                self.start = (self.start + 1) % len(self.queue)
                return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.start]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.end-1) % len(self.queue)]
        return -1

    def isEmpty(self) -> bool:
        return not self.full and self.start == self.end

    def isFull(self) -> bool:
        return self.full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()