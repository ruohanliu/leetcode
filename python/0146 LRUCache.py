from collections import OrderedDict
class LRUCache:
    """
        #design

        python dict.popitem() does not have last=False option. Use OrderedDict
        dict.move_to_end(last=True)
    """
    # use OrderedDict
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = value
            if len(self.cache) > self.cap:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
            self.cache[key] = value

# do not use OrderedDict
class Node():
    def __init__(self,key=None,val=None,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class DLinkedList:
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

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.ll = DLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.ll.insertNode(self.ll.deleteNode(node))
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key,value)
            self.cache[key] = node
            self.ll.insertNode(node)
            if len(self.cache) > self.cap:
                node = self.ll.deleteNode()
                del self.cache[node.key]
        else:
            node = self.cache[key]
            node.val = value
            self.ll.insertNode(self.ll.deleteNode(node))