from collections import defaultdict
class Node():
    def __init__(self,key=None,val=None,left=None,right=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.left = left
        self.right = right

class DLinkedList:
    """
        tail and head could merge to use one node instead
    """
    def __init__(self):
        self.tail = Node()
        self.head = Node()
        self.tail.right = self.head
        self.head.left = self.tail
    
    def deleteNode(self,node=None):
        if not node:
            node = self.tail.right
        node.left.right,node.right.left = node.right,node.left
        node.left=node.right=None
        return node

    def insertNode(self,node):
        node.left,node.right,self.head.left.right,self.head.left = self.head.left,self.head,node,node

    def isEmpty(self):
        return self.tail.right == self.head

class LFUCache:
    """
        #design #linkedlist #important

        edge case: capacity = 0
    """
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = defaultdict(DLinkedList)
        self.cap = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.freq[node.freq].deleteNode(node)
            if self.freq[node.freq].isEmpty():
                if self.minFreq == node.freq:
                    self.minFreq = node.freq+1
                del self.freq[node.freq]
            node.freq += 1
            self.freq[node.freq].insertNode(node)            
            return node.val

    def put(self, key: int, value: int) -> None:
        # edge case
        if self.cap == 0:
            return
        if key not in self.cache:
            if len(self.cache) == self.cap:
                ll = self.freq[self.minFreq]
                node = ll.deleteNode()
                if ll.isEmpty():
                    del self.freq[self.minFreq]
                    # edge case
                    self.minFreq = min(self.freq.keys()) if self.freq else 0
                del self.cache[node.key]

            node = Node(key,value)
            self.cache[key] = node
            self.freq[1].insertNode(node)
            self.minFreq = 1
        else:
            node = self.cache[key]
            node.val = value
            self.freq[node.freq].deleteNode(node)
            if self.freq[node.freq].isEmpty():
                if self.minFreq == node.freq:
                    self.minFreq = node.freq+1
                del self.freq[node.freq]
            node.freq += 1
            self.freq[node.freq].insertNode(node)
