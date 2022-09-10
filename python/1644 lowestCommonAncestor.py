class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            #lca
        """
        def dfs(root):
            nonlocal cnt
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                if root == p or root == q:
                    cnt += 1
                    return root
                if left and right:
                    return root
                return left or right

        cnt = 0
        node = dfs(root)
        if cnt == 2:
            return node
        return None