# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist
        """
        n1 = 0
        n2 = 0
        head = l1
        while head:
            n1 += 1
            head = head.next
        head = l2
        while head:
            n2 += 1
            head = head.next
        

        # add two number without caring about carryover. reverse the list
        curr1,curr2 = l1,l2
        prev = None
        while n1 and n2:
            val = 0
            if n1>=n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1<n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -=1
            node = ListNode(val)
            node.next = prev
            prev = node
        
        curr = node
        prev = None
        carryover = 0
        while curr:
            carryover,val = divmod(curr.val+carryover,10)
            curr.val = val
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        if carryover:
            head = ListNode(1)
            head.next = prev
        else:
            head = prev
        return head
            