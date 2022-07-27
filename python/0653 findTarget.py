# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
            #bst

            could use inorder traversal to produce a sorted list as well

            Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
        """
        def find(root):
            nonlocal seen
            if root:
                if k-root.val in seen:
                    return True
                seen.add(root.val)
                return find(root.left) or find(root.right)
        
        seen = set()
        return find(root)