# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            #prefixsum #tree #dfs #pathsum
        """
        def dfs(root):
            nonlocal prefixSum,ans,seen
            if root:
                prefixSum+=root.val
                if prefixSum == targetSum:
                    ans += 1
                ans += seen[prefixSum-targetSum]
                
                seen[prefixSum]+=1
                dfs(root.left)
                dfs(root.right)
                seen[prefixSum]-=1
                prefixSum -= root.val

        prefixSum = 0
        seen = defaultdict(int)
        ans = 0
        dfs(root)
        return ans