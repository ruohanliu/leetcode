class ListNode:
    def __init__(self,key=0,value=0,next=None):
        self.next = next
        self.key = key
        self.value = value
class MyHashMap:
    """
        #prime #sieve #linkedlist #hashmap #design

        find all prime numbers up to n: Sieve of Eratosthenes. start with p**2 then increment by p up to n
    """

    def __init__(self):
        n = 2500
        self.arr = [0] * (n+1)
        p = 2
        while True:
            self.prime = p
            self.arr[p] = 1
            p2 = p ** 2
            while p2 <= n:
                self.arr[p2] = 1
                p2+=p

            while p<=n and self.arr[p]==1:
                p+=1
            if p > n:
                break
        for i in range(self.prime):
            self.arr[i] = None
        

    def put(self, key: int, value: int) -> None:
        mod = key%self.prime
        if self.arr[mod] == None:
            self.arr[mod] = ListNode(key,value)
        else:
            curr = self.arr[mod]
            prev = None
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                prev = curr
                curr = curr.next
            prev.next = ListNode(key,value)
        return

    def get(self, key: int) -> int:
        mod = key%self.prime
        if self.arr[mod] == None:
            return -1
        else:
            curr = self.arr[mod]
            while curr:
                if curr.key == key:
                    return curr.value
                curr = curr.next
            return -1


    def remove(self, key: int) -> None:
        mod = key%self.prime
        if self.arr[mod] == None:
            return
        else:
            curr = self.arr[mod]
            sentinel = ListNode(next=curr)
            prev = sentinel
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    self.arr[mod] = sentinel.next
                    return
                prev = curr
                curr = curr.next
            return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

obs = MyHashMap()
