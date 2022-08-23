class FreqStack:
    """
        #design #stack    
    """
    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stack[self.freq[val]].append(val)
        self.maxf = max(self.maxf,self.freq[val])

    def pop(self) -> int:
        val = self.stack[self.maxf].pop()
        self.freq[val] -= 1
        if not self.stack[self.maxf]:
            del self.stack[self.maxf]
            self.maxf -= 1
        return val

