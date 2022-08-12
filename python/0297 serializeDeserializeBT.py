# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
        #serialization #tree
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(node):
            nonlocal ans
            if node:
                ans.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                ans.append("#")
            
        ans = []
        dfs(root)
        return " ".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            nonlocal it
            val = next(it)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        it = iter(data.split())
        return helper()
        