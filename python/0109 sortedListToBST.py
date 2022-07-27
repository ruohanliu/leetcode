# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
            #BST #tree #linkedlist
        """
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        def helper(lo,hi):
            nonlocal head
            if lo>hi:
                return None
            
            mid = (lo+hi)//2
            left = helper(lo,mid-1)
            
            
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = helper(mid+1,hi)
            
            return root
        return helper(0,size-1)
            