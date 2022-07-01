# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        """
            #BST #important

            target may not be in the tree.
        """
        if not root:
            return None,None
        elif target >= root.val:
            left,right = self.splitBST(root.right,target)
            root.right = left
            return root,right
        else:
            left,right = self.splitBST(root.left,target)
            root.left = right
            return left,root
