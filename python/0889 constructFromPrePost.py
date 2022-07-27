from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
            #binarytree #construct
            preorder + postorder => tree
            without using index map
        """
        def build():
            nonlocal preIndex,posIndex
            root = TreeNode(preorder[preIndex])
            preIndex += 1
            if (root.val != postorder[posIndex]):
                root.left = build()
            if (root.val != postorder[posIndex]):
                root.right = build()
            posIndex += 1
            return root

        preIndex, posIndex = 0, 0
        return build()