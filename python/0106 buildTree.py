from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
            #binarytree #construct

            inorder + postorder => tree

            inOrderIndex map is to check whether subtree exist
        """
        def helper(lo,hi):
            if lo > hi:
                return None
            root = TreeNode(postorder.pop())
            i = inOrderIndex[root.val]

            root.right = helper(i+1,hi)
            root.left = helper(lo,i-1)

            return root
        inOrderIndex = {val:i for i,val in enumerate(inorder)}
        return helper(0,len(postorder)-1)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
            without using index map
        """
        def build(bound=None):
            if not inorder or inorder[-1] == bound:
                return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)
            return root

        return build()
