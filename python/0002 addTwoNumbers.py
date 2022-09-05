class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist
        """
        lists = l1, l2
        sentinel = curr = ListNode(0)
        carry = 0
        while lists or carry:
            carry += sum(a.val for a in lists)
            lists = [a.next for a in lists if a.next]
            curr.next = curr = ListNode(carry % 10)
            carry //= 10
        return sentinel.next