class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        """
            #lca 
            related 236
        """
        def dfs(root,level):
            nonlocal ans
            if root:
                left = dfs(root.left,level+1)
                right = dfs(root.right,level+1)

                if root.val == p or root.val == q:
                    ans.append(level)
                    return root,level
                if left and right:
                    return root,level
                return left or right
            return None

        ans = []            
        lca,level = dfs(root,0)
        if lca.val in (p,q):
            return abs(level-ans[0])
        else:
            return sum(ans)-2*level