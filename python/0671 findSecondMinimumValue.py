# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        val = root.val
        queue = deque([root])
        minVal = float("inf")
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val > val:
                    minVal = min(minVal,node.val)
                elif node.left:
                    queue.append(node.left)
                    queue.append(node.right)
        return minVal if minVal < float("inf") else -1

    def findSecondMinimumValue(self, root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1