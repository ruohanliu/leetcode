from threading import Lock
class MyCircularDeque:
    """
        #deque #lock #design
        related 622
    """

    def __init__(self, k: int):
        self.queue = [0] * k
        self.start = 0
        self.end = 0
        self.full = False
        self.lock = Lock()

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            # automatically acquire the lock when entering the block
            with self.lock:
                self.start = (self.start - 1) % len(self.queue)
                self.queue[self.start] = value
                if self.start == self.end:
                    self.full = True
                return True
            # automatically release the lock when leaving the block
        return False

    def insertLast(self, value: int) -> bool:
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

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            with self.lock:
                if self.start == self.end:
                    self.full = False
                self.start = (self.start + 1) % len(self.queue)
                return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            with self.lock:
                if self.start == self.end:
                    self.full = False
                self.end = (self.end - 1) % len(self.queue)
                return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[self.start]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.end-1) % len(self.queue)]
        return -1
        
    def isEmpty(self) -> bool:
        return not self.full and self.start == self.end

    def isFull(self) -> bool:
        return self.full
