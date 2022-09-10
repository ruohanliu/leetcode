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
            #tree #construct #bst #preorder #important
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

    def bstFromPreorder(self, preorder):
        """
            O(n^2)
        """
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = bisect.bisect_left(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

    def bstFromPreorder(self, preorder):
        """
            O(nlogn)
        """
        def helper(i, j):
            if i == j: return None
            root = TreeNode(preorder[i])
            mid = bisect.bisect_left(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))

    def bstFromPreorder(self, preorder):
        """
            O(n)
        """
        def helper(A,upperBound):
            if not A or A[-1] > upperBound:
                return None
            node = TreeNode(A.pop())
            node.left = helper(A,node.val)
            node.right = helper(A,upperBound)
            return node
        return helper(preorder[::-1],float("inf"))