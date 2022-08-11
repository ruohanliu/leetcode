class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
            #dfs #tree
            related 549
        """
        # max path starting node
        def dfs(node):
            nonlocal ans
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                res = 1 + max(l if l and node.left.val == node.val + 1 else 0,r if r and node.right.val == node.val + 1 else 0)
                ans = max(ans,res)
                return res
            else:
                return 0
        ans = 0
        dfs(root)
        return ans