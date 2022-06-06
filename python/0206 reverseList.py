class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist #reverse
        """
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        