# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            #linkedlist #trick
        """
        lo = None
        hi = None
        curr = head
        cnt = 0
        while curr:
            cnt += 1
            if hi:
                hi = hi.next
            if cnt == k:
                lo = curr
                hi = head
            curr = curr.next
        hi.val,lo.val = lo.val,hi.val
        return head
            