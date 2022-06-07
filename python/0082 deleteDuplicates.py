# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist #sentinel

            save next node first thing in a loop
        """
        if not head:
            return None
        
        sentinel = ListNode(head)
        
        curr = head
        prev = sentinel
        dup = False
        while curr.next:
            next = curr.next
            if next.val == curr.val:
                dup = True
            else:
                if not dup:
                    prev.next = curr
                    prev = curr
                    prev.next = None
                dup = False
            curr = next
            
        if not dup:
            prev.next = curr

        return sentinel.next
        