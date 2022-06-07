# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        """
            #linkedlist #sentinel
            save next node first thing in a loop
            if unsure of next node, set curr.next = None
        """
        counter = defaultdict(int)
        curr = head
        while curr:
            counter[curr.val] += 1
            curr = curr.next

        sentinel = ListNode(head)
        curr = head
        prev = sentinel
        while curr:
            next = curr.next
            if counter[curr.val] == 1:
                prev.next = curr
                prev = curr
                prev.next = None
            curr = next

        return sentinel.next