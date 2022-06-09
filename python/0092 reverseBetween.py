from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            consider if left and right are starting and ending nodes

            possible with #recursion
        """

        i = 1
        curr = head
        n1 = None
        while i<left:
            n1 = curr
            curr = curr.next
            i += 1
        n2 = curr
        prev = None
        while i < right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
            
        # i == right
        n3 = curr
        n4 = curr.next
        curr.next = prev
        
        if n1:
            n1.next = n3
        else:
            head = n3
        n2.next = n4
        return head
