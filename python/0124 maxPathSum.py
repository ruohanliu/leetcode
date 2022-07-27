# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
            #recursion #pathsum #tree
        """
        # returns the max pathsum from this root
        def dfs(root):
            nonlocal ans
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                ans = max(ans,max(l,r,l+r,0)+root.val)
                return max(root.val,root.val+l,root.val+r)
            else:
                return 0
        ans = float("-inf")
        dfs(root)
        return ans
