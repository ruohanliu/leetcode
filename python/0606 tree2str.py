class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
            #tree #preorder
        """
        def dfs(root):
            nonlocal ans
            if root:
                ans.append(str(root.val))
                if root.left or root.right:
                    ans.append("(")
                if root.left:
                    dfs(root.left)
                if root.left or root.right:
                    ans.append(")")
                if root.right:
                    ans.append("(")
                    dfs(root.right)
                    ans.append(")")
        ans = []
        dfs(root)
        return "".join(ans)

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            if root.left == root.right:
                return str(root.val)
            if not root.right:
                return str(root.val) + "(" + self.tree2str(root.left) + ")"
            return str(root.val)+"(" + self.tree2str(root.left)+")(" + self.tree2str(root.right) + ")"
        else:
            return ""

    def tree2str(self, root: TreeNode) -> str:
        if not root: return ""
        stack = []
        stack.append(root)
        ans = ""
        while stack:
            node = stack.pop()
            if node == ')':
                ans += ')'
                continue

            ans += '(' + str(node.val)

            if not node.left and node.right:
                ans += '()'

            if node.right:
                stack.append(')')
                stack.append(node.right)

            if node.left:
                stack.append(')')
                stack.append(node.left)
                
        return ans[1:]