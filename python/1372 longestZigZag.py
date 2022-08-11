class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
            #tree $dfs
        """
        def dfs(node):
            if node:
                if node.left == node.right:
                    return (0,0,0)
                l = r = _ans = ans_ = 0
                if node.left:
                    _l,_r,_ans = dfs(node.left)
                    l = 1 + _r
                if node.right:
                    _l,_r,ans_ = dfs(node.right)
                    r = 1 + _l

                return (l,r,max([l,r,_ans,ans_]))

        return dfs(root)[2]