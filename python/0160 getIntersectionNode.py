# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
            naive 1: for every node in A, check if it is in B, O(mn) time
            naive 2: store node of A in set, compare with B, O(m or n) space
            best: observe that the 2 list share the common tail, if pointer A traverse a-tail-b,
                pointer B traverse b-tail-a, they will meet at the same time at intersection.
                if the 2 lists do not intersect, then both will be None when the loop ends.

            #linkedlist #math
        """
        posA = headA
        posB = headB
        while posA != posB:
            posA = headB if not posA else posA.next
            posB = headA if not posB else posB.next
        return posA
