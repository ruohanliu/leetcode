from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
            #tree #traverse #recursion
        """
        ans = []
        def traverse(root,h,l,r):
            nonlocal ans
            if not root:
                return
            if h:
                ans.append(root.val)
                traverse(root.left,False,True,False)
                traverse(root.right,False,False,True)
            elif l:
                ans.append(root.val)
                if root.left:
                    traverse(root.left,False,True,False)
                    traverse(root.right,False,False,False)
                else:
                    traverse(root.right,False,True,False)
            elif r:
                if root.right:
                    traverse(root.left,False,False,False)
                    traverse(root.right,False,False,True)
                else:
                    traverse(root.left,False,False,True)
                ans.append(root.val)
            else:
                if root.left == root.right:
                    ans.append(root.val)
                else:
                    traverse(root.left,False,False,False)
                    traverse(root.right,False,False,False)
        traverse(root,True,False,False)
        return ans