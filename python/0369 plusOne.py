# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
            #linkedlist
        """
        sentinel = ListNode(0)
        sentinel.next = head
        notNine = sentinel
        while head:
            if head.val != 9:
                notNine = head
            head = head.next
            
        notNine.val +=1
        while notNine.next:
            notNine = notNine.next
            notNine.val = 0
        return sentinel if sentinel.val else sentinel.next