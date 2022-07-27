# Definition for a binary tree node.
from inspect import stack
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
            #binarytree #recursion #morris #dfs
        """
        ans = 0
        number = 0
        def traverse(root):
            if not root:
                return
            
            nonlocal ans,number
            number <<= 1
            number |=root.val
            
            if not root.left and not root.right:
                ans += number
            traverse(root.left)
            traverse(root.right)
            
            number >>= 1
            return 
            
        traverse(root)
        return ans

    def sumRootToLeaf(self, root, val=0):
        """
            if root.left == root.right is a shortcut
        """
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
            #iteration #bfs
        """
        ans = 0
        node_stack = [(root,0)]
        while node_stack:
            node,number = node_stack.pop()
            number = (number << 1) | node.val
            if node.left:
                node_stack.append((node.left,number))
            if node.right:
                node_stack.append((node.right,number))
            if not root.left and not root.right:
                ans += number
        return ans