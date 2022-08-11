class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
            #BST
            related 98
        """
        def dfs(node):
            nonlocal ans
            if not node:
                return (float("inf"),float("-inf"),0)

            lmin,lmax,ln = dfs(node.left)
            rmin,rmax,rn = dfs(node.right)
            
            if lmax < node.val < rmin:
                ans = max(ans,ln+rn+1)
                return (min(lmin,node.val),max(rmax,node.val),ln+rn+1)
            else:
                return (float("-inf"),float("inf"),0)
                
        ans = 0
        dfs(root)
        return ans