# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
            #tree #BST #construct
        """
        def helper(i,j):
            if i>j:
                return [None]
            ans = []
            for k in range(i,j+1):
                left = helper(i,k-1)
                right = helper(k+1,j)
                for lnode in left:
                    for rnode in right:
                        ans.append(TreeNode(k,lnode,rnode))
            return ans
        
        return helper(1,n)      