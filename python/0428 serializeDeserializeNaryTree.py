"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    """
        #serialization #google
    """
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def dfs(node):
            nonlocal ans
            if node:
                ans.append(str(node.val))
                ans.append(str(len(node.children)))
                for child in node.children:
                    dfs(child)
            
        ans = []
        dfs(root)
        return " ".join(ans)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def helper():
            nonlocal it
            val = int(next(it))
            return Node(val,[helper() for _ in range(int(next(it)))])
            
        if data:
            it = iter(data.split())
            return helper()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))