# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    """
        #design #iter
    """
    def makeInteger(self):
        while self.stack:
            curr_list,curr_index = self.stack[-1]
            if len(curr_list) == curr_index:
                self.stack.pop()
                continue
            if curr_list[curr_index].isInteger():
                break
            next_list = curr_list[curr_index].getList()
            self.stack[-1][1] +=1
            self.stack.append([next_list,0])
        
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList,0]]
        
    def next(self) -> int:
        self.makeInteger()
        curr_list,curr_index = self.stack[-1]
        self.stack[-1][1] += 1
        return curr_list[curr_index]
    
    def hasNext(self) -> bool:
        self.makeInteger()
        return len(self.stack) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())