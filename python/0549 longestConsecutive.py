class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
            #dfs #tree
            related 298
        """
        # max ascending and descending path starting node
        def dfs(node):
            nonlocal ans
            if node:
                la,ld = dfs(node.left)
                ra,rd = dfs(node.right)
                d = max(ld if node.left and node.val - node.left.val == 1 else 0,\
                        rd if node.right and node.val - node.right.val == 1 else 0) + 1
                a = max(la if node.left and node.val - node.left.val == -1 else 0,\
                        ra if node.right and node.val - node.right.val == -1 else 0) + 1
                ans = max(ans,a+d-1)
                return (a,d)
            else:
                return (0,0)
        ans = 0
        dfs(root)
        return ans