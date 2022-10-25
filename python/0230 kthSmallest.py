# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            #BST #inorder
        """
        def bstGen(node):
            if node:
                yield from bstGen(node.left)
                yield node.val
                yield from bstGen(node.right)
        
        for i,val in enumerate(bstGen(root)):
            if i == k-1:
                return val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node = stack.pop()
            k-=1
            if k == 0:
                return node.val
            node = node.right