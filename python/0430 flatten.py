"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, node: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            start = node
            end = node
            while node:
                if node.child:
                    nextt = node.next
                    flattenedStart,flattenedEnd = helper(node.child)
                    flattenedStart.prev = node
                    node.child = None
                    flattenedEnd.next = nextt
                    node.next = flattenedStart
                    end = flattenedEnd
                    node = nextt
                    if node:
                        node.prev = end
                else:
                    end = node
                    node = node.next
            return (start,end)
        start,_ = helper(head)
        return start