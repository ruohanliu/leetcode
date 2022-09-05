# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist #prefixsum
        """
        sentinel = ListNode(0,head)
        curr = head
        ps = 0
        nodeIdx = {0:sentinel}
        while curr:
            ps += curr.val
            if ps in nodeIdx:
                prev = nodeIdx[ps]
                while ps in nodeIdx:
                    nodeIdx.popitem()
                nodeIdx[ps] = prev
                prev.next = curr.next
            else:
                nodeIdx[ps] = curr
            curr = curr.next

        return sentinel.next