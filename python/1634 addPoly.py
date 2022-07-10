# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
            #linkedlist
            when skipping node, make sure curr.next = None
        """
        sentinel = PolyNode()
        curr = sentinel
        while poly1 or poly2:
            if not poly1:
                curr.next = poly2
                break
            if not poly2:
                curr.next = poly1
                break
            if poly1.power<poly2.power:
                poly1,poly2=poly2,poly1
            if poly1.power == poly2.power:
                poly1.coefficient += poly2.coefficient
                if poly1.coefficient != 0:
                    curr.next = poly1
                    curr = poly1
                poly1 = poly1.next
                poly2 = poly2.next
            else:
                curr.next = poly1
                curr = poly1
                poly1 = poly1.next
            curr.next = None
        return sentinel.next
                
        