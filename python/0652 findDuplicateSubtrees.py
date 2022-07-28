# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
            #serialization
        """
        seen = Counter()
        ans = []
        def serialize(node):
            serialization = []
            if node:
                serialization.extend(serialize(node.right))
                serialization.extend(serialize(node.left))
                serialization.append(node.val)
            else:
                return ["#"]
            
            t = tuple(serialization)
            if seen[t] == 1:
                ans.append(node)
            seen[t]+=1
            return serialization
        serialize(root)
        return ans