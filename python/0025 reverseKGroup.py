from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            #linkedlist
        """
        cnt = 0
        sentinel = ListNode(next = head)

        prev = None
        curr = head
        grpCurr = curr
        grpPrev = sentinel
        while curr:
            cnt += 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if cnt == k:
                grpPrev.next = prev
                grpCurr.next = curr
                grpPrev = grpCurr
                grpCurr = curr
                cnt = 0

        curr = prev
        prev = None
        for i in range(cnt):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return sentinel.next



