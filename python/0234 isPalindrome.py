from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome_o1_space(self, head: Optional[ListNode]) -> bool:
        """
            #linkedlist #reverse #slownfast #inplace
        """
        def find_first_half(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_list(head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        if head is None:
            return True
        first_half_end = find_first_half(head)
        second_half_start = first_half_end.next
        end = reverse_list(second_half_start)
        while head and end:
            if head.val != end.val:
                return False
            head = head.next
            end = end.next

        first_half_end.next = reverse_list(end)
        return True