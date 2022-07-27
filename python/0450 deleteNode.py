# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            #BST
            delete node
        """
        def successor(root):
            prev = root
            root = root.right
            while root.left:
                prev = root
                root = root.left
            return (prev,root)
        
        def predecessor(root):
            prev = root
            root = root.left
            while root.right:
                prev = root
                root = root.right
            return (prev,root)
        
        def dfs(root,key):
            if root:
                if root.val == key:
                    if not root.right:
                        root =  root.left
                    elif not root.left:
                        root =  root.right
                    #both left and right child exist
                    else:
                        pParent, p = predecessor(root)
                        # in case the predecessor is directly connected to roo
                        if pParent != root:
                            pParent.right = p.left
                            p.left = root.left
                        p.right = root.right
                        root.left = None
                        root.right = None
                        root = p
                elif key <root.val:
                    root.left = dfs(root.left,key)
                else:
                    root.right = dfs(root.right,key)
                return root
            else:
                return None
        return dfs(root,key)
                    
                    
                