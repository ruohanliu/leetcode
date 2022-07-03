# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            #linkedlist #mergesort #important
        """
        def middle(node):
            slow = node
            fast = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow

        def merge(l1,l2):
            sentinel = ListNode()
            curr = sentinel
            while l1 or l2:
                if not l1:
                    curr.next = l2
                    break
                if not l2:
                    curr.next = l1
                    break
                if l1.val<=l2.val:
                    curr.next = l1
                    curr = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = l2
                    l2 = l2.next
                curr.next = None
            return sentinel.next
        
        def sort(node):
            if not node or not node.next:
                return node
            mid = middle(node)
            l1 = sort(node)
            l2 = sort(mid)
            return merge(l1,l2)
        
        return sort(head)