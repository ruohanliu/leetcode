# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            #tree #levelorder
        """
        queue = deque([(root,0)])
        ans = 0
        while queue:
            mn = float("inf")
            mx = float("-inf")
            for _ in range(len(queue)):
                node,pos = queue.popleft()
                mn = min(mn,pos)
                mx = max(mx,pos)
                if node.left:
                    queue.append((node.left,2*pos))
                if node.right:
                    queue.append((node.right,2*pos+1))
            ans = max(ans,mx-mn+1)
        return ans
        