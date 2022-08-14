class CountIntervals:
    """
        #segmenttree #sortedlist #important
        related 352 731 2158
        SortedList item is immutable, use pop(idx) and add() instead
    """
    def __init__(self):
        from sortedcontainers import SortedList
        self.range = SortedList()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        l = self.range.bisect_left((left,right))
        # because of sorting order, only need to check 1 left side but need to check multiple right side
        if l-1 >= 0:
            x,y = self.range[l-1]
            if y >= left:
                left = min(left,x)
                right = max(right,y)
                self.range.pop(l-1)
                self.cnt -= y-x+1
                l-=1
        while l < len(self.range):
            x,y = self.range[l]
            if x > right:
                break
            right = max(right,y)
            self.range.pop(l)
            self.cnt -= y-x+1
        self.range.add((left,right))
        self.cnt += right-left+1

    def count(self) -> int:
        return self.cnt

# segment tree
class Node:
    def __init__(self):
        self.res = 0
        self.left = None
        self.right = None
    def add(self,node,x,y,s,e):
        if e <= x or s >= y or (node and node.res == y-x):
            return node
        if not node:
            node = Node()
        if s<=x and y<=e:
            node.res = y-x
            return node 
        mid = (x+y)//2
        node.left = self.add(node.left,x,mid,s,e)
        node.right = self.add(node.right,mid,y,s,e)
        node.res = 0
        if node.left:
            node.res+=node.left.res
        if node.right:
            node.res+=node.right.res
        return node

class CountIntervals:

    def __init__(self):
        self.root = Node()

    def add(self, left: int, right: int) -> None:
        self.root.add(self.root,1,10**9+1,left,right+1)

    def count(self) -> int:
        return self.root.res
        