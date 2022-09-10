"""
    #google #important #databricks
"""
class Node:
    def __init__(self):
        self.left, self.right = None, None
        self.length = 0
        self.value = None

    def print(self):
        if self.left: self.left.print()
        if self.right: self.right.print()
        if self.value:
            print(self.value, end="")

class Cord:
    def __init__(self, largestr, limit=5):
        def buildtree(i, j):
            length = j-i
            node = Node()
            if length > limit:
                node.left = buildtree(i, length // 2)
                node.right = buildtree(length // 2, j)
            else:
                node.value = largestr[i:j]
            node.length = length
            return node
        self.root = buildtree(0, len(largestr))

    def print(self):
        self.root.print()
        print()

    def merge(self, other):
        newRoot = Node()
        newRoot.left = self.root
        newRoot.right = other.root
        newRoot.length = self.root.length + other.root.length
        self.root = newRoot

    def char_at(self, index, node=None):
        if node is None:
            node = self.root
    
        if index >= node.length:
            return None
            
        if node.value: return node.value[index]
        
        search = None
        if index < node.left.length:
            search = node.left
        else:
            search = node.right
            index -= node.left.length
        return self.char_at(index, search)

    def substr(self, start, end, node=None):
        if node is None:
            node = self.root

        start = max(0, start)
        end = min(end, start + node.length)
        if node.value:
            return node.value[start:end]
        
        left = ""
        if start < node.left.length: # value at left
            left = self.substr(start, end, node.left)
            
        right = ""
        if end > node.left.length:
            right = self.substr(start - node.left.length, end - node.left.length, node.right)
        return left + right
        
    def delete(self, index, node = None):
        if node is None:
            node = self.root
        if index >= node.length:
            return

        if node.value:
            node.value = node.value[:index] + node.value[index+1:]
            node.length-=1
            return
        
        if index < node.left.length:
            self.delete(index, node.left)
        else:
            self.delete(index-node.left.length, node.right)
        node.length-=1
        
test = Cord("0123456789")

print(test.char_at(2))
print(test.char_at(6))
print(test.substr(2, 7))

test.print()
print(test.substr(2,4))

test.delete(3) # delete char 3
print(test.char_at(3)) # this should print 4
test.print()