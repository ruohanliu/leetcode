# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            #BST #important
        
            building BST need indices for its left and right subtree and value for its root.
        """
        def helper(lo,hi):
            nonlocal preOrderIndex
            if lo > hi:
                return None
            
            root = TreeNode(preorder[preOrderIndex])
            
            preOrderIndex += 1
            root.left = helper(lo,inOrderIndex[root.val]-1)
            root.right = helper(inOrderIndex[root.val]+1,hi)
            
            return root
        
        preOrderIndex = 0
        inOrderIndex = {v:i for i,v in enumerate(inorder)}
        return helper(0,len(inorder)-1)