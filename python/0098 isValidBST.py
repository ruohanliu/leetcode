class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
            #BST
            related 333
        """
        def helper(node,lo,hi):
            if not node:
                return True

            if (lo != None and node.val <=lo) or (hi != None and node.val >=hi):
                return False

            return helper(node.left,lo,node.val) and helper(node.right,node.val,hi)
                
        return helper(root,None,None)