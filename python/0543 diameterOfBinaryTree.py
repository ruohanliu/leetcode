# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            #binarytree #nonlocal #recursion
        """
        
        maxDiameter = 0
        def helper(root):
            nonlocal maxDiameter
            if root.left:
                leftHeight = helper(root.left) + 1
            else:
                leftHeight = 0
            if root.right:
                rightHeight = helper(root.right) + 1
            else:
                rightHeight = 0
                
            maxDiameter = max(maxDiameter,leftHeight+rightHeight)
            return max(leftHeight,rightHeight)
        
        helper(root)
        return maxDiameter
        