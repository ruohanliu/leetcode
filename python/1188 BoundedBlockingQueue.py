import threading
class BoundedBlockingQueue(object):
    """
        #threading #Semaphore #Condition
        deque implemented is cpython is threadsafe
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.queue = deque()
        self.pull = threading.Semaphore(0)
        self.push = threading.Semaphore(capacity)

    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.queue.append(element)
        self.pull.release()

    def dequeue(self) -> int:
        self.pull.acquire()
        x = self.queue.popleft()
        self.push.release()
        return x

    def size(self) -> int:
        return len(self.queue)
        

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.q=deque([])
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        self.cond.acquire()
        while self.size()==self.capacity:
            self.cond.wait()
        self.q.append(element)
        self.cond.notifyAll()
        self.cond.release()

    def dequeue(self) -> int:
        self.cond.acquire()
        while len(self.q)==0:
            self.cond.wait()
        x= self.q.popleft()
        self.cond.notifyAll()
        self.cond.release()
        return x

    def size(self) -> int:
        return len(self.q)