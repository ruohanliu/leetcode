# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
            #greedy #tree #recursion #important
            
            Steps:
            1. Set cameras on all leaves' parents, thenremove all covered nodes.
            2. Repeat step 1 until all nodes are covered.            
            
            You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

            Return the minimum number of cameras needed to monitor all nodes of the tree.
        """
        def dfs(node):
            nonlocal ans
            if not node:
                return "null"
            if node.left == node.right:
                return "leaf"
            l,r = dfs(node.left),dfs(node.right)
            if l == "leaf" or r == "leaf":
                ans += 1
                return "camera"
            if l == "camera" or r == "camera":
                return "null"
            else:
                return "leaf"
            
        ans = 0
        return (dfs(root) == "leaf") + ans