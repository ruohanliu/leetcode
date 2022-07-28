class RangeModule:
    """
        #segmenttree #sortedlist #important

        SortedList item is immutable, use pop(idx) and add() instead
    """

    def __init__(self):
        from sortedcontainers import SortedList
        self.range = SortedList()

    def addRange(self, left: int, right: int) -> None:
        l = self.range.bisect_left((left,right))
        while l-1 >= 0:
            x,y = self.range[l-1]
            if y<left:
                break
            left = min(left,x)
            right = max(right,y)
            self.range.pop(l-1)
            l-=1
        while l < len(self.range):
            x,y = self.range[l]
            if x > right:
                break
            right = max(right,y)
            self.range.pop(l)
        self.range.add((left,right))

    def queryRange(self, left: int, right: int) -> bool:
        l = self.range.bisect_left((left,right))
        return (l > 0 and self.range[l-1][1] >= right) or (l<len(self.range) and self.range[l][0] == left and self.range[l][1] >= right)

    def removeRange(self, left: int, right: int) -> None:
        l = self.range.bisect_left((left,right))
        if l-1 >= 0:
            x,y = self.range[l-1]
            if y>left:
                self.range.pop(l-1)
                self.range.add((x,left))
                if y > right:
                    self.range.add((right,y))
                
        while l < len(self.range):
            x,y = self.range[l]
            if y <= right:
                self.range.pop(l)
            else:
                if x <= right:
                    self.range.pop(l)
                    self.range.add((right,y))
                break

# segment tree
class Node:
    def __init__(self,l,r,cover):
        self.cover = cover
        self.left = None
        self.right = None
        self.l = l
        self.r = r

class RangeModule:

    def __init__(self):
        self.root = Node(1,10**9,False)

    def updateRange(self,node,cover,left,right):
        if right< node.l or left > node.r:
            return
        if left<=node.l and node.r <= right:
            node.cover = cover
            # purge all children if current node range is updated
            node.left=None
            node.right=None
            return
        if not node.left:
            mid = (node.l+node.r)//2
            node.left=Node(node.l,mid,node.cover)
            node.right=Node(mid+1,node.r,node.cover)
        self.updateRange(node.left,cover,left,right)
        self.updateRange(node.right,cover,left,right)
        node.cover = node.left.cover and node.right.cover

    def addRange(self, left: int, right: int) -> None:
        self.updateRange(self.root,True,left,right-1)

    def removeRange(self, left: int, right: int) -> None:
        self.updateRange(self.root,False,left,right-1)
        
    def queryRange(self, left: int, right: int) -> bool:
        def query(node):
            if right < node.l or node.r < left:
                return True
            
            if (left <= node.l and node.r <= right) or not node.left: # either node contained by q or cover is same for whole node.
                return node.cover
            
            return query(node.left) and query(node.right)
        
        right -= 1
        return query(self.root)
