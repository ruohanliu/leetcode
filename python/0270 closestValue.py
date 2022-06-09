# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
            #BST #trim #iterate
        """    
        min_diff = float("inf")
        res = 0
        def traverse(root):
            if not root:
                return
            nonlocal min_diff,res
            if abs(root.val-target) < min_diff:
                min_diff = abs(root.val-target)
                res = root.val
            if min_diff == 0:
                return
            elif root.val-target > 0:
                traverse(root.left)
            else:
                traverse(root.right)
        traverse(root)
        return res

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float("inf")
        res = 0
        while root and min_diff > 0:
            diff = root.val-target
            if abs(diff) < min_diff:
                min_diff = abs(diff)
                res = root.val
            if diff > 0:
                root = root.left
            else:
                root = root.right
        return res