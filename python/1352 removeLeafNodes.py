# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
            #tree
        """
        def dfs(node,parent,l):
            if node.left:
                dfs(node.left,node,True)
            if node.right:
                dfs(node.right,node,False)

            if not node.left and not node.right:
                if node.val == target:
                    if l:
                        parent.left = None
                    else:
                        parent.right = None

        if not root:
            return None

        sentinel = TreeNode()
        sentinel.left = root
        dfs(root,sentinel,True)
        if sentinel.left:
            return root
        else:
            return None

    def removeLeafNodes(self, root, target):
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root