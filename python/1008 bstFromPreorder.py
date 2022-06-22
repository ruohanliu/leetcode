from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]
        root = stack[0]
        n = len(preorder)
        for i in range(1, n):
            node = stack[-1]
            newNode = TreeNode(preorder[i])
            while stack and stack[-1].val < newNode.val:
                node = stack.pop()
            if newNode.val < node.val:
                node.left = newNode
            else:
                node.right = newNode
            stack.append(newNode)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
            #binarytree #construct #binarysearchtree
        """
        def build(lo,hi):
            nonlocal preIndex
            if preIndex >= len(preorder) or preorder[preIndex] <= lo or preorder[preIndex] >= hi:
                return None

            root = TreeNode(preorder[preIndex])
            preIndex += 1
            root.left = build(lo,root.val)
            root.right = build(root.val,hi)
            return root
        preIndex = 0
        return build(float("-inf"),float("inf"))
