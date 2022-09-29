from time import time
"""
    #ratelimit
"""
class TokenBucket:
    def __init__(self,capacity,refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill_ts = time()

    def allow(self,tokens):
        self.refill()
        if tokens <= self.tokens:
            self.tokens -= tokens
            return True
        else:
            return False
    def refill(self):
        if self.tokens < self.capacity:
            now = time()
            _tokens = self.refill_rate * (now - self.last_refill_ts)
            self.tokens = min(self.capacity,self.tokens + _tokens)
            self.last_refill_ts = now

class LeakyBucket:
    def __init__(self,capacity,refill_rate):
        self.capacity = capacity
        self.used = 0
        self.refill_rate = refill_rate
        self.ts = time()

    def allow(self,tokens):
        now = time()
        self.used = max(0,self.used - (now - self.ts) * self.refill_rate)
        if self.used < self.capacity:
            self.used += 1
            self.ts = now
            return True
        else:
            return False

class SlidingWindow:

    def __init__(self, capacity, time_unit, forward_callback, drop_callback):
        self.capacity = capacity
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

        self.ts = time()
        self.pre_count = capacity
        self.cur_count = 0

    def handle(self, packet):
        now = time()
        if now - self.ts > self.time_unit:
            self.ts = time()
            self.pre_count = self.cur_count
            self.cur_count = 0

        ec = (self.pre_count * (self.time_unit - (now-self.ts)) / self.time_unit) + self.cur_count

        if (ec >= self.capacity):
            return self.drop_callback(packet)

        self.cur_count += 1
        return self.forward_callback(packet)


def forward(packet):
    print("Packet Forwarded: " + str(packet))


def drop(packet):
    print("Packet Dropped: " + str(packet))

throttle = SlidingWindow(5, 1, forward, drop)